import sys
import time
import numpy as np

import algs
from models import *

NO_LOG = False
NUM_SIM = 1

MODEL_POOL = [
    FacenetModel64, #FacenetModel128, FacenetModel256,
    VggnetModel256,
    GooglenetModel128,
    Inception4Model256,
    Resnet50Model128, #Resnet50Model256, Resnet50Model512,
    DcganModel256,
    ChatbotModel256,
    VideopredictionModel64
]
ALGS = [
    # 'brute_force_ne',
    'srtf_ne',
    'srsf_ne',
    # 'srtf_relaxed',
    # 'tiresias_las',
    'max_min',
    'max_speedup',
    'opt_2jobs',
    'opt_gs',
    'opt_tsgs',
    'optimus',
    'heuristic',
    'brute_force',
]
INF = float('inf')

def log(msg, end='\n'):
    if not NO_LOG:
        sys.stderr.write('%s%s' % (msg, end))

class Trace(object):
    def __init__(self, model_pool, avg_interval, total_num):
        self.model_pool = model_pool
        self.avg_interval = avg_interval
        trace = []
        abs_time = 0
        for _ in range(total_num):
            rand_model = model_pool[np.random.randint(0, len(model_pool))]
            trace.append((abs_time, rand_model))
            abs_time += np.random.poisson(avg_interval)
        self.trace = tuple(trace)

class Scheduler(object):
    def __init__(self, alg, total_gpus, trace):
        self.unfinished = []
        self.finished = []
        self.max_running_jobs = 0
        self.total_gpus = total_gpus
        self.trace = trace
        self.current_time = 0
        self.current_trace_idx = 0
        self.assign = algs.__dict__[alg]
    
    def continue_until_next_event(self):
        # Check the nearest event from unfinished jobs
        if len(self.unfinished) > self.max_running_jobs:
            self.max_running_jobs = len(self.unfinished)
        if len(self.unfinished) > 0:
            nearest_event_time = min([m.next_event_time for m in self.unfinished])
        else:
            nearest_event_time = INF
        # Check the nearest job arrival event
        if self.current_trace_idx < len(self.trace):
            arrival_time, model = self.trace[self.current_trace_idx]
        else:
            arrival_time = INF
        # Continue until the nearest event occurs
        if nearest_event_time <= arrival_time:
            next_event_time = nearest_event_time
            arrival = False
        else:
            next_event_time = arrival_time
            arrival = True
        # print('NEXT_EVENT: %f, ARRIVAL: %f' % (next_event_time, arrival_time))
        unfinished = []
        for m in self.unfinished:
            # Add very little amount of time to surely trigger the event
            m.continue_until(next_event_time + 1e-5)
            if m.is_finished:
                self.finished.append(m)
                log(m.finish_info())
            else:
                unfinished.append(m)
        self.unfinished = unfinished
        self.current_time = next_event_time
        # Add the next job if this is a job arrival event
        if arrival:
            self.current_trace_idx += 1
            self.unfinished.append(model(self.current_time))
        # Assign GPUs to all jobs
        if len(self.unfinished) > 0:
            self.assign(self.unfinished, self.total_gpus)
        log('%.1f,%s' % (self.current_time,
                str([(m.name, m.gpus, m.remain_iter) for m in self.unfinished])))
        assert(self.total_gpus >= sum([m.gpus for m in self.unfinished]))

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
        sum_elapsed = sum([m.current_time - m.arrival_time for m in sched.finished])
        avg_elapsed = sum_elapsed / num_models
        # sys.stderr.write('=== Alg: %s ===\n' % alg)
        # sys.stderr.write('Avg JCT:       %.2f\n' % (sched.avg_elapsed()/3600.))
        # sys.stderr.write('Avg wait time: %.2f\n' % (sched.avg_wait()/3600.))
        # sys.stderr.write('Avg run time:  %.2f\n' % ((sched.avg_elapsed() - sched.avg_wait())/3600.))
        # sys.stderr.write('Makespan:      %.2f\n' % (sched.timestamp/3600.))
        ret = avg_elapsed/3600.
    print('%.6f,' % ret, end='')
    return ret

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
        tr = Trace(MODEL_POOL, avg_interval, num_models)
        rets = [run_sim(a, num_gpus, tr.trace) for a in ALGS]
        min_ret = min(rets)
        for i, r in enumerate(rets):
            if abs(r - min_ret) < 1e-4:
                wins[i] += 1
        print('')
    print('\n== Result ==')
    for i, a in enumerate(ALGS):
        print('%s:\t%d' % (a, wins[i]))
