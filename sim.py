import os
import io
import sys
import json
import time
import itertools
import math
import heapq
import pickle
import string
import random
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from collections import namedtuple

import algs
import models
from philly_job import PhillyJob

import ray

INF = float('inf')
TraceEntry = namedtuple('TraceEntry', ['ts', 'model', 'iters', 'max_gpus', 'req_gpus'])

PRINT_TRACE = False
DRAW_FIGURE = False
SCALE = 1

vgg16 = models.VggnetModel256()
googlenet = models.GooglenetModel128()
inception4 = models.Inception4Model256()
resnet50 = models.Resnet50Model128()
deepspeech = models.DeepspeechModel64()
# autoencoder = models.AutoencoderModel51200()
# transformer = models.TransformerModel4096()
transformer = models.TransformerModel256()
dcgan = models.DcganModel256()
chatbot = models.ChatbotModel256()
video = models.VideopredictionModel64()
MODEL_POOL = [vgg16, googlenet, inception4, resnet50, deepspeech,
    # autoencoder,
    transformer,
    dcgan, chatbot, video]

ALGS = [
    "FIFO_ELASTIC",
    "SRSF_ELASTIC"
    # "FIFO_ELASTIC",
    # 'FIFO'
    # 'Tiresias',
    # 'SRTF',
    # 'SRSF',
    # 'Optimus',
    # 'MaxMin',
    # 'OptPP',
    # 'Opt2Jobs',
    # 'OptBoundary',
    # '100,10',
]

RANDCODE_CHARS = string.ascii_letters + string.digits

random.seed(time.time())

def randcode():
    return ''.join(random.choice(RANDCODE_CHARS) for _ in range(8))

class Job(object):
    def __init__(self, jid, ts_arrival, model, iters, max_gpus, req_gpus):
        # Constants.
        self.jid = jid
        self.ts_arrival = ts_arrival
        self.model = model
        self.iters = iters
        self.max_gpus = max_gpus
        self.req_gpus = req_gpus
        # Status.
        self.ts_current = ts_arrival
        self.ts_exp_fin = INF
        self.ts_evicted = ts_arrival
        self.ts_init_scheduled = INF
        self.ts_scheduled = INF
        self.ts_next_event = INF

        self.remain_iters = iters
        self.gpus = 0
        self.tpi = INF
        self.is_finished = False
        # For Tiresias only.
        self.tiresias_tj = 0
        self.tiresias_evicted = False
        self.tiresias_starving = False
        # For OptPP only.
        self.optpp_sched_cnt = 0
        #
        self.tmp_gpus = None

        self.sched_history = [(self.ts_current, self.gpus, self.remain_iters)]
        # self.gpu_allocation_history = []

    def __lt__(self, job):
        return self.jid < job.jid

    def continue_until(self, ts):
        if ts >= self.ts_exp_fin:
            self.remain_iters = 0
            self.is_finished = True
            self.ts_current = self.ts_exp_fin
            self.ts_next_event = INF
        elif self.gpus > 0:
            ts_diff = ts - self.ts_current
            if ts_diff > 0:
                self.remain_iters -= ts_diff / self.tpi
                self.ts_exp_fin = math.ceil(ts + self.remain_iters * self.tpi)
            self.ts_current = ts
        else:
            self.ts_current = ts

    def schedule(self, num_gpus, ts_next_event=INF, available_gpus=0):
        if self.gpus == 0 and num_gpus > 0:
            if self.ts_init_scheduled == INF:
                self.ts_init_scheduled = self.ts_current
            self.ts_scheduled = self.ts_current
            self.ts_evicted = INF
            self.tpi = self.model.times_per_iter[num_gpus - 1]
            self.ts_exp_fin = math.ceil(self.ts_current + self.remain_iters * self.tpi)
        elif self.gpus > 0 and num_gpus == 0:
            self.ts_evicted = self.ts_current
            self.ts_scheduled = INF
            self.tpi = INF
            self.ts_exp_fin = INF
        elif num_gpus == 0:
            assert(self.tpi == INF)
            assert(self.ts_exp_fin == INF)
        elif num_gpus > 0:
            if num_gpus != self.gpus:
                self.tpi = self.model.times_per_iter[num_gpus - 1]
            ts_exp_fin = math.ceil(self.ts_current + self.remain_iters * self.tpi)
            if self.gpus == num_gpus and abs(self.ts_exp_fin - ts_exp_fin) > ts_exp_fin * 0.1:
                print('%d, %d' % (self.ts_exp_fin, ts_exp_fin), flush=True)
            else:
                self.ts_exp_fin = ts_exp_fin
        if ts_next_event == INF:
            self.ts_next_event = self.ts_exp_fin
        else:
            self.ts_next_event = min(math.ceil(ts_next_event), self.ts_exp_fin)
        if self.gpus != num_gpus:
            self.sched_history.append((self.ts_current, num_gpus, self.remain_iters, available_gpus))
        
        self.gpus = num_gpus

    def exp_remain_time(self, num_gpus):
        if num_gpus <= 0:
            return INF
        return self.remain_iters * self.model.times_per_iter[num_gpus - 1]

    def times_per_iter(self, num_gpus):
        if num_gpus <= 0:
            return INF
        return self.model.times_per_iter[num_gpus - 1]

    def throughput(self, num_gpus):
        if num_gpus <= 0:
            return 0
        return self.model.throughputs[num_gpus - 1]

    def dp(self, num_gpus):
        return self.model.dps[num_gpus]

    def rdp(self, num_gpus):
        return self.model.rdps[num_gpus]

    def sojourn_time(self):
        return self.ts_current - self.ts_arrival

class Scheduler(object):
    def __init__(self, alg, total_gpus, trace):
        self.ts = 0
        self.assign = algs.__dict__[alg]
        # For testing Tiresias
        # t, k = alg.split(',')
        # self.assign = lambda jobs, total_gpus: algs.tiresias_las(
        #     jobs, total_gpus, thres=float(t)*3600, starvation_knob=float(k), relaxed=False)
        self.total_gpus = total_gpus
        self.jobs_run = []
        self.jobs_fin = []
        self.arrival_events = []
        ts = -1
        cnt = itertools.count()
        for te in trace:
            job = Job(next(cnt), *te)
            next_ts = math.ceil(te.ts)
            if ts == next_ts:
                self.arrival_events[-1].append((next_ts, job.jid, job))
            else:
                ts = next_ts
                self.arrival_events.append([(next_ts, job.jid, job)])
        self.arrival_events.reverse()
        self.events = self.arrival_events.pop()
        self.availability_history = []


    def is_done(self):
        return len(self.events) == 0

    def continue_next_event(self):
        # Process events.
        if len(self.events) == 0:
            raise RuntimeError('No more events')
        next_ts = self.events[0][0]
        for ts, jid, job in self.events:
            if job is not None:
                self.jobs_run.append(job)
        # Make progress of all jobs.
        new_fins = []
        running = []
        for job in self.jobs_run:
            job.continue_until(next_ts)
            if job.is_finished:
                new_fins.append(job)
            else:
                running.append(job)
        self.ts = next_ts
        self.jobs_run = running
        self.jobs_fin.extend(new_fins)
        if not self.jobs_run:
            if self.arrival_events:
                self.events = self.arrival_events.pop()
            else:
                self.events.clear()
        else:
            # Run GPU allocation algorithm.
            self.assign(self.jobs_run, self.total_gpus)
            ts_nearest_event = INF
            nearest_event_jobs = []
            for job in self.jobs_run:
                if job.ts_next_event < ts_nearest_event:
                    ts_nearest_event = job.ts_next_event
                    nearest_event_jobs = [job]
                elif job.ts_next_event == ts_nearest_event:
                    nearest_event_jobs.append(job)
            if self.arrival_events:
                ts_nearest_arrival = self.arrival_events[-1][0][0]
            else:
                ts_nearest_arrival = INF
            if ts_nearest_event < ts_nearest_arrival:
                self.events = [(math.ceil(job.ts_next_event), job.jid, None)
                    for job in nearest_event_jobs]
            elif ts_nearest_event > ts_nearest_arrival:
                self.events = self.arrival_events.pop()
            else:
                if ts_nearest_event == INF:
                    print([(j.jid, j.gpus, j.ts_next_event) for j in self.jobs_run], flush=True)
                    assert(False)
                self.events = self.arrival_events.pop()
                self.events.extend([(math.ceil(job.ts_next_event), job.jid, None)
                    for job in nearest_event_jobs])
            # Verification.
            num_assigned_gpus = sum([j.gpus for j in self.jobs_run])
            
            self.availability_history.append((self.ts, self.total_gpus - num_assigned_gpus))
            if num_assigned_gpus > self.total_gpus:
                raise RuntimeError('Allocated GPUs more than total: %d / %d' % (
                    num_assigned_gpus, self.total_gpus))

def gen_philly_trace(vc, scale, follow_gpu_req=False, num_offline=0):
    VC = ['0e4a51', '103959', '11cb48', '2869ce', '51b7ef', '6214e9',
        '6c71a0', '7f04ca', 'b436b2', 'e13805', 'ed69ec', 'ee9e8c']
    assert(vc in VC)
    PHILLY_LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'philly-traces/trace-data/cluster_job_log')
    PHILLY_MACHINE_LIST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'philly-traces/trace-data/cluster_machine_list')
    with io.open(PHILLY_LOG_PATH, 'r') as f:
        cluster_job_log = json.load(f)
    jobs = []
    for j in cluster_job_log:
        job = PhillyJob(**j)
        if job.vc != vc:
            continue
        if job.service_time is None:
            continue
        if job.num_gpus == 0 or job.num_gpus is None:
            continue
        jobs.append((job.submitted_time.timestamp(), job))
    jobs.sort(key=lambda x: x[0])
    start = jobs[0][0]
    trace = []
    np.random.seed(0)
    for idx, tup in enumerate(jobs):
        ts, job = tup
        pool = [m for m in MODEL_POOL if m.max_gpus >= job.num_gpus]
        if len(pool) == 0:
            continue
        m = pool[np.random.randint(0, len(pool))]
        if follow_gpu_req:
            mgpus = job.num_gpus
        else:
            mgpus = m.max_gpus
        serv_time = job.service_time * 60 * scale + 0
        iters = serv_time / m.times_per_iter[job.num_gpus - 1]
        if iters < 1:
            continue
            # iters = 1
        # Running a part of trace
        # if ts - start <= 47 * 3600 * 24:
        #     continue
        # elif ts - start > int(53 * 3600 * 24):
        #     continue
        trace.append(TraceEntry(
            ts=(ts - start) * scale, model=m, iters=iters,
            max_gpus=mgpus, req_gpus=job.num_gpus))
    # rescaled = []
    # for e in trace:
    #     rescaled.append(TraceEntry(
    #         ts=e.ts * 1, model=e.model, iters=e.iters * 1,
    #         max_gpus=e.max_gpus, req_gpus=e.req_gpus))
    # trace = rescaled
    if num_offline > 0:
        random.seed(time.time())
        rand_entries = random.choices(trace, k=num_offline)
        trace.clear()
        for e in rand_entries:
            trace.append(TraceEntry(
                ts=0, model=e.model, iters=e.iters,
                max_gpus=e.max_gpus, req_gpus=e.req_gpus))
    if PRINT_TRACE:
        prev_time = 0
        last_time = 0
        for te in trace:
            if isinstance(te.model, models.VggnetModel256):
                model_name = 'vgg16'
                bs = 256
            elif isinstance(te.model, models.GooglenetModel128):
                model_name = 'googlenet'
                bs = 128
            elif isinstance(te.model, models.Inception4Model256):
                model_name = 'inception4'
                bs = 256
            elif isinstance(te.model, models.Resnet50Model128):
                model_name = 'resnet50'
                bs = 128
            elif isinstance(te.model, models.DeepspeechModel64):
                model_name = 'deepspeech'
                bs = 64
            elif isinstance(te.model, models.AutoencoderModel51200):
                model_name = 'autoencoder'
                bs = 51200
            elif isinstance(te.model, models.TransformerModel4096):
                model_name = 'transformer'
                bs = 4096
            elif isinstance(te.model, models.TransformerModel256):
                model_name = 'transformer'
                bs = 256
            elif isinstance(te.model, models.DcganModel256):
                model_name = 'dcgan'
                bs = 256
            elif isinstance(te.model, models.ChatbotModel256):
                model_name = 'chatbot'
                bs = 256
            elif isinstance(te.model, models.VideopredictionModel64):
                model_name = 'video'
                bs = 64
            else:
                assert(False)
            start_time = te.ts - prev_time
            prev_time = te.ts
            print(str({"model": model_name, "bs": bs,
                "iter": int(te.iters), "job_name": "%s_%s" % (model_name, randcode()),
                "req": te.req_gpus, "start_time": "%d" % start_time}) + ',')
        sys.exit(0)
    return trace

def gen_tiresias_trace(num_offline):
    pool_2 = [m for m in MODEL_POOL if m.max_gpus >= 2]
    pool_4 = [m for m in MODEL_POOL if m.max_gpus >= 4]
    pool_8 = [m for m in MODEL_POOL if m.max_gpus >= 8]
    pool_16 = [m for m in MODEL_POOL if m.max_gpus >= 16]
    pool_32 = [m for m in MODEL_POOL if m.max_gpus >= 32]
    model_list = []
    for _ in range(40):
        model_list.append((2, pool_2[np.random.randint(0, len(pool_2))]))
    for _ in range(80):
        model_list.append((4, pool_4[np.random.randint(0, len(pool_4))]))
    for _ in range(90):
        model_list.append((8, pool_8[np.random.randint(0, len(pool_8))]))
    for _ in range(25):
        model_list.append((16, pool_16[np.random.randint(0, len(pool_16))]))
    for _ in range(5):
        model_list.append((32, pool_32[np.random.randint(0, len(pool_32))]))
    random.shuffle(model_list)
    trace = []
    ts = 0
    for ngpu, m in model_list:
        serv_time = 120 + np.random.rand() * (7200 - 120)
        iters = 0
        while iters < 1:
            iters = serv_time / m.times_per_iter[ngpu - 1]
        trace.append(TraceEntry(
            ts=ts, model=m, iters=iters, max_gpus=ngpu, req_gpus=ngpu))
        # Poisson random interval (avg 30 sec).
        ts += np.random.poisson(30)

    if num_offline > 0:
        random.seed(time.time())
        rand_entries = random.choices(trace, k=num_offline)
        trace.clear()
        for e in rand_entries:
            trace.append(TraceEntry(
                ts=0, model=e.model, iters=e.iters,
                max_gpus=e.max_gpus, req_gpus=e.req_gpus))
    return trace

_COLORS = {'Tiresias-L': 'C0', 'SRTF': 'C1', 'max-min': 'C2',
    'Opt2Jobs': 'C5', 'SRSF': 'C4', 'OptPP': 'C3'}

def draw(draw_info, is_vertical=False, sharex=False):
    num = len(draw_info)
    if is_vertical:
        fig, axes = plt.subplots(num, 1, sharex=sharex)
        fig.set_size_inches(2.5, 1.4 * num)
    else:
        fig, axes = plt.subplots(1, num, sharex=sharex)
        fig.set_size_inches(2.5, 2.8)
    for ax, info in zip(axes, draw_info):
        draw_type, fig_info = info
        if draw_type == 'step' or draw_type == 'plot':
            data, xlabel, ylabel, legend, is_log, ws, xlim, ylim = fig_info
            legend_handles = []
            for alg, v in data.items():
                x, y, color = v
                if ws > 1:
                    wy = []
                    for i in range(1, ws):
                        wy.append(sum(y[:i]) / i)
                    rec = 1 / ws
                    for i in range(ws, len(y) + 1):
                        wy.append(sum(y[i - ws:i]) * rec)
                else:
                    wy = y
                if draw_type == 'step':
                    ax.step(x, wy, label=alg, color=color, where='post', linewidth=.6)
                else:
                    ax.plot(x, wy, label=alg, color=color, linewidth=.6)
                legend_handles.append(mpatches.Patch(color=color, label=alg))
            if not sharex or not is_vertical:
                ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            if is_log:
                ax.set_yscale('log')
                ax.axhline(y=1, color='black', linewidth=1, linestyle='-')
            if legend != '':
                ax.legend(handles=legend_handles, loc=legend, ncol=2, fontsize='x-small')
            if xlim:
                ax.set_xlim(*xlim)
            if ylim:
                ax.set_ylim(*ylim)
        elif draw_type == 'bar':
            data, xlabel, ylabel = fig_info
            idx = 0
            for alg, v in data.items():
                val, color = v
                rects = ax.bar([idx], [val], label=alg, width=.5)
                rect = rects[0]
                ax.annotate('%.1f' % val,
                    xy=(rect.get_x() + rect.get_width() / 2, val),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')
                idx += 1
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
        ax.grid(alpha=.3, linestyle='--')
        ax.tick_params(axis="x",direction="in")
        ax.tick_params(axis="y",direction="in")
    if sharex and is_vertical:
        ax.set_xlabel(xlabel)


@ray.remote
def main(vc, alg, num_gpus=64):
    num_offline = 0
    trace_follow_req = gen_philly_trace(vc, SCALE, True, num_offline)
    trace_no_follow_req = gen_philly_trace(vc, SCALE, False, num_offline)
    # trace_follow_req = gen_tiresias_trace(num_offline)
    # trace_no_follow_req = trace_follow_req
    total_gpus = num_gpus
    results = []

    if alg == 'Tiresias' or alg == 'SRTF' or alg == 'SRSF':
        trace = trace_follow_req
    elif alg == 'MaxMin' or ('Opt' in alg):
        trace = trace_no_follow_req
    else:
        trace = trace_follow_req
    cnt = 0
    sched = Scheduler(alg, total_gpus, trace)
    while not sched.is_done():
        sched.continue_next_event()
        if cnt == 0:
            print(alg, sched.ts, len(sched.jobs_run), flush=True)
            cnt = 1000
        cnt -= 1
    print(alg, sched.ts, len(sched.jobs_run), flush=True)
    if len(sched.jobs_run) > 0 or len(sched.jobs_fin) != len(trace):
        raise RuntimeError('Scheduler finished unexpectedly: '
            'running %d, finished %d, total %d' % (
                len(sched.jobs_run), len(sched.jobs_fin), len(trace)))
    # Summarize results.
    if alg == 'Tiresias':
        alg = 'Tiresias-L'
    elif alg == 'MaxMin':
        alg = 'max-min'
    elif 'OptPP' in alg:
        alg = 'LRR-P'
    elif alg == 'Opt2Jobs':
        alg = 'LRR-L'


    return [vc, alg, num_gpus, sched]

    results.append((alg, sched.jobs_fin))



    # Print ACTs first.
    acts = {}

    for alg, jobs in results:

        with open(f"job_sched_history_{vc}_{alg}_{num_gpus}.pkl",'wb') as fp:
            pickle.dump(jobs,fp)

        with open(f"sched_sched_history_{vc}_{alg}_{num_gpus}.pkl",'wb') as fp:
            pickle.dump(sched.availability_history,fp)
        
        # preemption_data = [len(j.sched_history) for j in jobs]
        # preemption_data.sort()
        # cdf = np.linspace(0,1,len(preemption_data))

        # plt.figure()
        # plt.plot(preemption_data, cdf)
        # plt.savefig(f"preemption_data_{vc}_{alg}.png", dpi=300)

        act = sum([j.sojourn_time() for j in jobs]) / len(jobs) / 60.
        acts[alg] = [act, _COLORS.get(alg, None)]
    print(vc, [a[0] for a in acts.values()], flush=True)
    # with io.open('results_%s.pkl' % vc, 'wb') as f:
    #     pickle.dump(results, f)
    if not DRAW_FIGURE:
        return
    # with io.open('results_%s.pkl' % vc, 'rb') as f:
    #     results = pickle.load(f)

    # Plot details.
    qls = {}
    fts = {}
    sis = {}
    for i, res in enumerate(results):
        alg, jobs = res
        history = []
        for j in jobs:
            history.append((j.ts_arrival, j, -1, j.iters))
            for ts, ngpu, rem in j.sched_history:
                history.append((ts, j, ngpu, rem))
            history.append((j.ts_current, j, -2, 0))
        history.sort()
        grouped = [[history[0]]]
        for hi in history[1:]:
            if grouped[-1][0][0] == hi[0]:
                grouped[-1].append(hi)
            else:
                grouped.append([hi])
        times = []
        ql = []
        ft = []
        si = []
        util = []
        cur_jobs = {}
        for g in grouped:
            for hi in g:
                ts, job, num, rem = hi
                if num == -1:
                    cur_jobs[job] = (0, 0, rem, ts)
                elif num == -2:
                    del cur_jobs[job]
                elif num == 0:
                    if cur_jobs[job][0] > 0:
                        cur_jobs[job] = (0, 0, rem, ts)
                else:
                    cur_jobs[job] = (num, job.model.speedups[num - 1], rem, None)
            day = ts / 3600. / 24.
            times.append(day)
            running_jobs = []
            pending_jobs = []
            for job, info in cur_jobs.items():
                if info[0] > 0:
                    running_jobs.append((job, info))
                else:
                    pending_jobs.append((job, info))
            if running_jobs:
                ft.append(sum([1./(job.iters * job.model.times_per_iter[info[0] - 1]) if info[2] > 0 else 0 \
                    for job, info in running_jobs]))
            else:
                ft.append(float('inf'))
            if pending_jobs:
                si.append(sum([(ts - info[3]) / (info[2] * job.model.times_per_iter[0]) if info[2] > 0 else 0 \
                    for job, info in pending_jobs]) / len(pending_jobs))
            else:
                si.append(0)
            ql.append(len(cur_jobs) - len(running_jobs))
        times.append(times[-1] + 1e-5)
        ql.append(0)
        ft.append(float('inf'))
        si.append(0)
        qls[alg] = [times, ql, _COLORS.get(alg, None)]
        fts[alg] = [times, ft, _COLORS.get(alg, None)]
        sis[alg] = [times, si, _COLORS.get(alg, None)]
    #
    draw([
        # ('bar', acts),
        ('step', [qls, 'Time (days)', 'QL', 'upper left', False, 1, None, None]),
        ('step', [fts, 'Time (days)', 'Sum. FT', '', True, 200, None, (0.005, 0.4)]),
        ('step', [sis, 'Time (days)', 'Avg. BI', '', True, 1, None, None]),
    ], is_vertical=True, sharex=True)
    plt.subplots_adjust(left=.24, right=.99, bottom=.1, top=1.)
    plt.savefig("results_run.png")

if __name__ == '__main__':

    ray.init()

    futures = list()

    # for num_gpus in 
    for alg in ALGS:
        # for num_gpus in [100,200,300,400,500]:
        for num_gpus in [100]:
            for vc in [
                # 'ed69ec',
                # '11cb48',
                # '2869ce',
                # '103959',
                # 'ee9e8c',
                # '7f04ca',
                # 'e13805',
                # '6c71a0',
                # 'b436b2',
                # '6214e9',
                '0e4a51',
                ]:
                    futures.append(main.remote(vc,alg,num_gpus=num_gpus))

    finished = ray.get(futures)

    for result in finished:
        vc, alg, num_gpus, sched = result

        with open(f"job_sched_history_{vc}_{alg}_{num_gpus}.pkl",'wb') as fp:
            pickle.dump(sched.jobs_fin,fp)

        with open(f"sched_sched_history_{vc}_{alg}_{num_gpus}.pkl",'wb') as fp:
            pickle.dump(sched.availability_history,fp)







