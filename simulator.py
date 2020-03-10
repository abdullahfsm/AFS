import sys
import time
import io
import os
import json
import pickle
import random
import string
import random
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

import algs
from plot import plot_show
from models import *
from philly_job import PhillyJob

NO_LOG = True
PRINT_PLOT = True
PRINT_TRACE = False
NUM_SIM = 1
VC = '0e4a51'

PHILLY_LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    'philly-traces/trace-data/cluster_job_log')

MODEL_POOL = [
    VggnetModel256,
    GooglenetModel128,
    Inception4Model256,
    Resnet50Model128,
    DeepspeechModel64,
    AutoencoderModel51200,
    TransformerModel4096,
    DcganModel256,
    ChatbotModel256,
    VideopredictionModel64
]
# MODEL_POOL_CNN = [
#     VggnetModel256,
#     GooglenetModel128,
#     Inception4Model256,
#     Resnet50Model128, #Resnet50Model256, Resnet50Model512,
# ]
# MODEL_POOL = MODEL_POOL_CNN
MODEL_POOL_2 = [m.__class__ for m in [x() for x in MODEL_POOL] if m.max_gpus >= 2]
MODEL_POOL_4 = [m.__class__ for m in [x() for x in MODEL_POOL] if m.max_gpus >= 4]
MODEL_POOL_8 = [m.__class__ for m in [x() for x in MODEL_POOL] if m.max_gpus >= 8]
MODEL_POOL_16 = [m.__class__ for m in [x() for x in MODEL_POOL] if m.max_gpus >= 16]
MODEL_POOL_32 = [m.__class__ for m in [x() for x in MODEL_POOL] if m.max_gpus >= 32]
ALGS = [
    # 'brute_force',
    # 'fifo',
    'srtf',
    'srsf',
    # 'fifo_relaxed',
    # 'srtf_relaxed',
    # 'srsf_relaxed',
    'tiresias_1',
    'tiresias_2',
    'tiresias_5',
    'tiresias_10',
    'tiresias_1_starve',
    'tiresias_2_starve',
    'tiresias_5_starve',
    'tiresias_10_starve',
    'max_min',
    'optimus',
    'alg_c_rough',
    'alg_c',
    'alg_c_eq',
    # 'alg_c_eq2',
    # 'max_speedup',
    # 'opt_pp',
    'opt_pp_2',
    # 'opt_boundary',
    # 'opt_greedy',
]
INF = float('inf')

RANDCODE_CHARS = string.ascii_letters + string.digits

random.seed(time.time())

def randcode():
    return ''.join(random.choice(RANDCODE_CHARS) for _ in range(16))

def log(msg, end='\n'):
    if not NO_LOG:
        sys.stderr.write('%s%s' % (str(msg), end))

class Trace(object):
    def __init__(self, model_pool, avg_interval, total_num):
        self.model_pool = model_pool
        self.avg_interval = avg_interval
        trace = []
        abs_time = 0
        for _ in range(total_num):
            rand_model = model_pool[np.random.randint(0, len(model_pool))]
            trace.append((abs_time, rand_model()))
            abs_time += int(np.random.poisson(avg_interval))
        self.trace = tuple(trace)

class ManualTrace(object):
    def __init__(self, model_pool, avg_interval, total_num):
        self.model_pool = model_pool
        self.avg_interval = avg_interval
        trace = [(1, Inception4Model256())]
        for i in range(10):
            j = DcganModel256()
            j.philly_request = 8
            trace.append((i*26760, j))
        self.trace = tuple(trace)

class DcganTrace(object):
    def __init__(self, model_pool, avg_interval, total_num):
        self.model_pool = model_pool
        self.avg_interval = avg_interval
        trace = []
        abs_time = 0
        for _ in range(total_num):
            model = DcganModel256()
            model.total_iter *= 10.
            model.remain_iter *= 10.
            trace.append((abs_time, model.submit(0, max_gpus=np.random.randint(1, 64))))
            abs_time += int(np.random.poisson(avg_interval))
        self.trace = tuple(trace)

class TiresiasTrace(object):
    def __init__(self, model_pool, avg_interval=3600, total_num=480):
        def random_length():
            return 120 + np.random.rand() * (7200 - 120)
            # return None
        self.model_pool = model_pool
        self.avg_interval = avg_interval
        models = []
        for i in range(int(total_num * 40 / 240)):
            rand_model = MODEL_POOL_2[np.random.randint(0, len(MODEL_POOL_2))]()
            models.append(rand_model.submit(0, max_gpus=2, length=random_length()))
        for i in range(int(total_num * 80 / 240)):
            rand_model = MODEL_POOL_4[np.random.randint(0, len(MODEL_POOL_4))]()
            models.append(rand_model.submit(0, max_gpus=4, length=random_length()))
        for i in range(int(total_num * 90 / 240)):
            rand_model = MODEL_POOL_8[np.random.randint(0, len(MODEL_POOL_8))]()
            models.append(rand_model.submit(0, max_gpus=8, length=random_length()))
        for i in range(int(total_num * 25 / 240)):
            rand_model = MODEL_POOL_16[np.random.randint(0, len(MODEL_POOL_16))]()
            models.append(rand_model.submit(0, max_gpus=16, length=random_length()))
        for i in range(int(total_num * 5 / 240)):
            rand_model = MODEL_POOL_32[np.random.randint(0, len(MODEL_POOL_32))]()
            models.append(rand_model.submit(0, max_gpus=32, length=random_length()))
        random.shuffle(models)
        trace = []
        abs_time = 0
        for rand_model in models:
            trace.append((abs_time, rand_model.submit(abs_time)))
            abs_time += int(np.random.poisson(avg_interval))
        self.trace = tuple(trace)

class PhillyTrace(object):
    def __init__(self, model_pool, avg_interval, total_num):
        self.model_pool = model_pool
        self.avg_interval = avg_interval

        with io.open(PHILLY_LOG_PATH, 'r') as f:
            cluster_job_log = json.load(f)
        jobs = []
        vcjobs = {}
        max_gpu_req = max((x().max_gpus for x in MODEL_POOL))
        for j in cluster_job_log:
            job = PhillyJob(**j)
            if job.run_time is None:
                continue
            if job.num_gpus == 0 or job.num_gpus is None:
                continue
            if job.num_gpus > max_gpu_req:
                continue
            x = vcjobs.get(job.vc, None)
            if x is None:
                vcjobs[job.vc] = [job]
            else:
                x.append(job)
        for vc, jobs in sorted(vcjobs.items()):
            if vc != VC:
                continue
            jobs.sort(key=lambda j: j.submitted_time.timestamp())
            # jobs = jobs[1055:1562]
            ips = {}
            reqs = {}
            max_fin = 0
            for job in jobs:
                x = reqs.get(job.num_gpus, None)
                if x is None:
                    reqs[job.num_gpus] = 1
                else:
                    reqs[job.num_gpus] += 1
                for at in job.attempts:
                    for d in at['detail']:
                        ip = d['ip']
                        ips[ip] = max((ips.get(ip, 0), len(d["gpus"])))
                fin = job.submitted_time.timestamp() + job.run_time
                if max_fin < fin:
                    max_fin = fin
            print('VC %s: #IP %d, #GPUs %d, #jobs %d, elapsed %.1f days, reqs %s' % (
                vc, len(ips), sum(ips.values()), len(jobs),
                (max_fin - jobs[0].submitted_time.timestamp()) / 24 / 3600,
                str(reqs)
            ))
            start = jobs[0].submitted_time.timestamp()
            models = []
            for j in jobs:
                # if total_num <= 0:
                #     break
                pool = [m.__class__ for m in [x() for x in MODEL_POOL] if m.max_gpus >= j.num_gpus]
                # if len(pool) == 0:
                #     continue
                assert(len(pool) > 0)
                rand_model = pool[np.random.randint(0, len(pool))]()
                rand_model.philly_request = rand_model.max_gpus
                # rand_model.philly_request = rand_model.num_gpus_for_speedup(0.5)
                models.append(rand_model.submit(j.submitted_time.timestamp() - start,
                    # max_gpus=j.num_gpus,
                    length=j.run_time,
                    # length_gpus=j.num_gpus))
                    length_gpus=rand_model.max_gpus))
                # total_num -= 1
            # fig, ax = plt.subplots()
            # ax.hist([m.philly_request for m in models], bins=64)
            # plt.show()
            self.trace = tuple(((m.arrival_time, m) for m in models))
            # stime = self.trace[0][0]
            # new_tr = []
            # for x in self.trace:
            #     if x[0] < stime + 3600 * 24 * 34 + 3000:
            #         continue
            #     if x[0] > stime + 3600 * 24 * 41:
            #         continue
            #     new_tr.append((x[0] - 3600 * 24 * 34 - 3000, x[1]))
            # self.trace = tuple(new_tr)
            if PRINT_TRACE:
                scale = 100
                ttt = []
                for i in range(len(self.trace)):
                    # if i % 4 == 0:
                    t, m = self.trace[i]
                    m.total_iter = int(m.total_iter/scale)
                    if m.total_iter == 0:
                        m.total_iter = 1
                    ttt.append((int(t/scale), m))
                ttt = tuple(ttt)
                self.trace = ttt
                prev_time = 0
                last_time = 0
                bursts = {}
                cnt = 0
                for t in ttt:
                    start_time = t[0] - prev_time
                    cnt += 1
                    if t[0] - last_time > 60:
                        if cnt > 10:
                            bursts[last_time] = str(cnt)
                        cnt = 0
                        last_time = t[0]
                    if isinstance(t[1], VggnetModel256):
                        model_name = 'vgg16'
                        bs = 256
                    elif isinstance(t[1], GooglenetModel128):
                        model_name = 'googlenet'
                        bs = 128
                    elif isinstance(t[1], Inception4Model256):
                        model_name = 'inception4'
                        bs = 256
                    elif isinstance(t[1], Resnet50Model128):
                        model_name = 'resnet50'
                        bs = 128
                    elif isinstance(t[1], DeepspeechModel64):
                        model_name = 'deepspeech'
                        bs = 64
                    elif isinstance(t[1], AutoencoderModel51200):
                        model_name = 'autoencoder'
                        bs = 51200
                    elif isinstance(t[1], TransformerModel4096):
                        model_name = 'transformer'
                        bs = 4096
                    elif isinstance(t[1], DcganModel256):
                        model_name = 'dcgan'
                        bs = 256
                    elif isinstance(t[1], ChatbotModel256):
                        model_name = 'chatbot'
                        bs = 256
                    elif isinstance(t[1], VideopredictionModel64):
                        model_name = 'video'
                        bs = 64
                    else:
                        assert(False)
                    prev_time = t[0]
                    iteration = t[1].total_iter
                    print(str({"model": model_name, "bs": bs,
                        "iter": iteration, "job_name": "%s_%s" % (model_name, randcode()),
                        "req": t[1].philly_request, "start_time": "%d" % start_time}) + ',')
                # print(str(vc) + ',' + ','.join(bursts.values()), flush=True)
                print('#bursts=%d' % len(bursts), flush=True)
        # sys.exit(0)

class Scheduler(object):
    def __init__(self, alg, total_gpus, trace):
        self.unfinished = []
        self.finished = []
        self.total_gpus = total_gpus
        self.trace = trace
        self.current_time = 0
        self.current_trace_idx = 0
        self.state = OrderedDict()
        self.assign = algs.__dict__[alg]
        self.alg = alg
        self.prog_data = []
        for _, m in self.trace:
            m.init()

    def act(self):
        total_num = len(self.finished) + len(self.unfinished)
        if total_num == 0:
            return 0
        sct = 0
        for j in self.finished:
            sct += j.total_runtime
        for j in self.unfinished:
            sct += j.total_runtime
        return float(sct)/total_num

    def mst(self):
        if len(self.unfinished) == 0:
            return 0
        else:
            return max([j.total_runtime for j in self.unfinished])

    def eff(self):
        s = 0
        for j in self.finished:
            s += j.total_iter * j.times_per_iter[0]
        return s

    def continue_until_next_event(self):
        # Check the nearest event from unfinished jobs
        if len(self.unfinished) > 0:
            nearest_event_time = min([m.next_event_time for m in self.unfinished])
        else:
            nearest_event_time = INF
        # Check the nearest job arrival event
        if self.current_trace_idx < len(self.trace):
            arrival_time, model = self.trace[self.current_trace_idx]
            assert(arrival_time != INF)
        else:
            arrival_time = INF
        # Continue until the nearest event occurs
        if nearest_event_time <= arrival_time:
            next_event_time = nearest_event_time
            arrival = False
        else:
            next_event_time = arrival_time
            arrival = True
            self.current_trace_idx += 1
        if next_event_time == INF:
            raise RuntimeError('Algorithm %s scheduled no jobs even though '
                               '%d waiting job(s) exist.' % (self.alg, len(self.unfinished)))
        next_event_time = int(next_event_time + 0.999999)
        if next_event_time == self.current_time:
            next_event_time += 1
        elif next_event_time < self.current_time:
            next_event_time = self.current_time
        # print('NEXT_EVENT: %f, ARRIVAL: %f' % (next_event_time, arrival_time))
        new_finished = []
        unfinished = []
        # Add the next job if this is a job arrival event
        if arrival:
            unfinished.append(model.submit(next_event_time))
        for m in self.unfinished:
            # Add very little amount of time to surely trigger the event
            m.continue_until(next_event_time)
            if m.is_finished:
                new_finished.append(m)
            else:
                unfinished.append(m)
        for m in new_finished:
            log(m.finish_info())
        if arrival or new_finished:
            # Before
            self.prog_data.append((next_event_time, self.act(), len(self.unfinished), self.mst(), self.eff()))
        self.finished.extend(new_finished)
        self.unfinished = unfinished
        self.current_time = next_event_time
        if arrival or new_finished:
            # After
            self.prog_data.append((next_event_time, self.act(), len(self.unfinished), self.mst(), self.eff()))
        # Assign GPUs to all jobs
        if len(self.unfinished) > 0:
            self.assign(self.unfinished, self.total_gpus, self.state)
        log('%d,%s' % (self.current_time,
                str([(m.name, m.gpus, m.remain_iter) for m in self.unfinished])))
        if not self.total_gpus >= sum([m.gpus for m in self.unfinished]):
            raise Exception('Invalid allocation of total %d GPUs: %s' % \
                    (self.total_gpus, str([m.gpus for m in self.unfinished])))

def run_sim(alg, num_gpus, trace):
    sched = Scheduler(alg, num_gpus, trace)
    num_models = len(trace)

    err = 0
    while sched.current_trace_idx != num_models or len(sched.unfinished) > 0:
        sched.continue_until_next_event()
        if sched.current_time == INF:
            log('error: starving forever')
            err = 1
            break
    # Print simulation results
    if err:
        ret = INF
    else:
        assert(len(sched.finished) == num_models)
        sum_elapsed = sum([m.total_runtime for m in sched.finished])
        avg_elapsed = sum_elapsed / num_models
        # sys.stderr.write('=== Alg: %s ===\n' % alg)
        # sys.stderr.write('Avg JCT:       %.2f\n' % (sched.avg_elapsed()/3600.))
        # sys.stderr.write('Avg wait time: %.2f\n' % (sched.avg_wait()/3600.))
        # sys.stderr.write('Avg run time:  %.2f\n' % ((sched.avg_elapsed() - sched.avg_wait())/3600.))
        # sys.stderr.write('Makespan:      %.2f\n' % (sched.timestamp/3600.))
        ret = avg_elapsed/3600.
    log('')
    print('%.6f,' % ret, end='')
    return ret, sched.prog_data

def print_usage():
    print('usage: python3 simulator.py NUM_GPUS NUM_MODELS AVG_INTV\n'
          '  NUM_GPUS:      Total number of GPUs to allocate\n'
          '  NUM_MODELS:    Total number of models to sumbit\n'
          '  AVG_INTV:      Average arrival interval between models\n')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print_usage()
        sys.exit(1)
    num_gpus = int(sys.argv[1])
    num_models = int(sys.argv[2])
    avg_interval = float(sys.argv[3])

    wins = [0] * len(ALGS)
    for n in range(NUM_SIM):
        tr = PhillyTrace(MODEL_POOL, avg_interval, num_models)
        rets = []
        if PRINT_PLOT:
            fig, [ax_act, ax_qlen, ax_msoj, ax_util] = plt.subplots(1, 4, sharex=False)
        max_act = 0
        last_time = 0
        prog_data_ctime_list = []
        prog_data_act_list = []
        prog_data_qlen_list = []
        prog_data_msoj_list = []
        prog_data_util_list = []
        for a in ALGS:
            ret, prog_data = run_sim(a, num_gpus, tr.trace)
            rets.append(ret)
            if PRINT_PLOT:
                prog_data_ctime = []
                prog_data_act = []
                prog_data_qlen = []
                prog_data_msoj = []
                prog_data_util = []
                for ctime, act, qlen, msoj, util in prog_data:
                    prog_data_ctime.append(ctime/3600./24.)
                    prog_data_act.append(act/3600.)
                    prog_data_qlen.append(qlen)
                    prog_data_msoj.append(msoj/3600.)
                    prog_data_util.append(util/num_gpus*100.)
                    max_act = max(max_act, prog_data_act[-1])
                prog_data_ctime_list.append(prog_data_ctime)
                prog_data_act_list.append(prog_data_act)
                prog_data_qlen_list.append(prog_data_qlen)
                prog_data_msoj_list.append(prog_data_msoj)
                prog_data_util_list.append(prog_data_util)
                last_time = max(last_time, prog_data_ctime[-1])
        if PRINT_PLOT:
            for i, a in enumerate(ALGS):
                prog_data_ctime_list[i].append(last_time * 1.03)
                prog_data_act_list[i].append(prog_data_act_list[i][-1])
                prog_data_qlen_list[i].append(prog_data_qlen_list[i][-1])
                prog_data_msoj_list[i].append(prog_data_msoj_list[i][-1])
                prog_data_util_list[i].append(prog_data_util_list[i][-1])
                ax_act.plot(prog_data_ctime_list[i], prog_data_act_list[i], label=a)
                ax_qlen.plot(prog_data_ctime_list[i], prog_data_qlen_list[i], label=a)
                ax_msoj.plot(prog_data_ctime_list[i], prog_data_msoj_list[i], label=a)
                ax_util.plot(prog_data_ctime_list[i], prog_data_util_list[i], label=a)
        min_ret = min(rets)
        for i, r in enumerate(rets):
            if abs(r - min_ret) < 1e-4:
                wins[i] += 1
        if PRINT_PLOT:
            # plot_show(fig, (ax_act, ax_qlen, ax_msoj, ax_util))
            with io.open('plot_%d.pkl' % time.time(), 'wb') as f:
                pickle.dump((VC, ax_act, ax_qlen, ax_msoj, ax_util), f)
            with io.open('plot_latest.pkl', 'wb') as f:
                pickle.dump((VC, ax_act, ax_qlen, ax_msoj, ax_util), f)
            plt.close()
            plot_show(VC, ax_act, ax_qlen, ax_msoj, ax_util)
        print('')
    print('\n== Result ==')
    for i, a in enumerate(ALGS):
        print('%s:\t%d' % (a, wins[i]))
