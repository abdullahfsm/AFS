import io
import os
import json
from philly_job import PhillyJob

PHILLY_LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    'philly-traces/trace-data/cluster_job_log')
PHILLY_MACHINE_LIST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    'philly-traces/trace-data/cluster_machine_list')

if __name__ == '__main__':
    cluster_machine_list = {}
    with io.open(PHILLY_MACHINE_LIST_PATH, 'r') as f:
        f.readline()
        for l in f.readlines():
            tkns = l.split(',')
            cluster_machine_list[tkns[0]] = (tkns[0], int(tkns[1]), tkns[2])
    with io.open(PHILLY_LOG_PATH, 'r') as f:
        cluster_job_log = json.load(f)

    alljobs = []
    vcjobs = {}
    for j in cluster_job_log:
        job = PhillyJob(**j)
        if job.service_time is None:
            continue
        if job.num_gpus == 0 or job.num_gpus is None:
            continue
        x = vcjobs.get(job.vc, None)
        if x is None:
            vcjobs[job.vc] = [job]
        else:
            x.append(job)
        alljobs.append(job)

    alljobs.sort(key=lambda j: j.submitted_time.timestamp())
    base_time = alljobs[0].submitted_time.timestamp()

    ips = {}
    reqs = {}
    max_fin = 0
    for job in alljobs:
        x = reqs.get(job.num_gpus, None)
        if x is None:
            reqs[job.num_gpus] = 1
        else:
            reqs[job.num_gpus] += 1
        for at in job.attempts:
            for d in at['detail']:
                ip = d['ip']
                ips[ip] = max((ips.get(ip, 0), len(d["gpus"])))
        fin = job.completed_time.timestamp()
        if max_fin < fin:
            max_fin = fin
    philly_total_gpus = sum([cluster_machine_list[ip][1] for ip in ips])
    print('Total: #IP %d, #GPUs %d, #jobs %d, elapsed %.1f days, reqs %s' % (
        len(ips), philly_total_gpus, len(alljobs),
        (max_fin - base_time) / 24 / 3600, str(reqs)
    ))

    all_events = []
    for job in alljobs:
        all_events.append((job.submitted_time.timestamp() - base_time, job.num_gpus))
        all_events.append((job.attempts[0]['end_time'].timestamp() - base_time, -job.num_gpus))
        for a in job.attempts[1:]:
            all_events.append((a['start_time'].timestamp() - base_time, job.num_gpus))
            all_events.append((a['end_time'].timestamp() - base_time, -job.num_gpus))
    all_events.sort(key=lambda ev: ev[0])
    cur_gpus = 0
    cur_time = 0
    non_idle_time = 0
    undersubscribed_time = 0
    for ev in all_events:
        elapsed = ev[0] - cur_time
        if cur_gpus > 0:
            non_idle_time += elapsed
            if cur_gpus <= 0.5 * philly_total_gpus:
                undersubscribed_time += elapsed
        cur_time = ev[0]
        cur_gpus += ev[1]
    print('%d / %d = %.3f' % (
        undersubscribed_time, non_idle_time,
        undersubscribed_time / non_idle_time), flush=True)