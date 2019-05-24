
from itertools import permutations

INF = float('inf')

def round_robin(request_list, total_amount):
    """Return a list of allocated # of resources in Round-Robin manner.

      Args:
        request_list:   (list) requested amounts in integer each.
        total_amount:   (int) total amount to assign.
    
      Returns:
        List of assigned amounts in integer each, remaining amount of resource
    """
    assign_list = [0] * len(request_list)
    all_done = False
    while total_amount > 0 and not all_done:
        all_done = True
        for i, req in enumerate(request_list):
            if req > assign_list[i]:
                all_done = False
                assign_list[i] += 1
                total_amount -= 1
                if total_amount == 0:
                    break
    return assign_list, total_amount

################################################################################

def max_min(jobs, total_gpus):
    req_list = [m.max_gpus for m in jobs]
    alloc_list, _ = round_robin(req_list, total_gpus)
    for i, m in enumerate(jobs):
        m.schedule(alloc_list[i])

def brute_force_ne(jobs, total_gpus):
    num = len(jobs)
    orders = permutations(range(num), num)
    min_sum_jct = INF
    min_order = None
    for order in orders:
        remains = [m.remain(m.max_gpus) for m in jobs]
        sum_jct = 0
        order_copy = [o for o in order]
        for i in range(num):
            min_remain = INF
            min_idx = -1
            slot = []
            gpus = total_gpus
            for idx in order_copy:
                m = jobs[idx]
                if gpus < m.max_gpus:
                    continue
                gpus -= m.max_gpus
                r = remains[idx]
                if r < min_remain:
                    min_remain = r
                    min_idx = idx
                slot.append(idx)
            for idx in slot:
                remains[idx] -= min_remain
            order_copy.remove(min_idx)
            sum_jct += min_remain * (num - i)
        if sum_jct < min_sum_jct:
            min_sum_jct = sum_jct
            min_order = order

    gpus = total_gpus
    for idx in min_order:
        m = jobs[idx]
        if gpus < m.max_gpus:
            m.schedule(0)
        else:
            gpus -= m.max_gpus
            m.schedule(m.max_gpus)

def brute_force(jobs, total_gpus):
    def gen_dist_helper(curs, mins, reqs, total, idx):
        if idx < len(curs) - 1:
            if sum(reqs[idx:]) < total:
                curs[idx:] = reqs[idx:]
                yield
            else:
                for g in range(mins[idx], min(total, reqs[idx]) + 1):
                    curs[idx] = g
                    for _ in gen_dist_helper(curs, mins, reqs, total - g, idx + 1):
                        yield
        else:
            c = min(total, reqs[idx])
            if c >= mins[idx]:
                curs[idx] = c
                yield

    def gen_dist(jobs, curs, total, mins=None, iters=None):
        n = len(jobs)
        reqs = [j.max_gpus for j in jobs]
        if mins is None:
            mins = [0] * n
        if iters is None:
            iters = [j.remain_iter for j in jobs]
        if n == 1:
            g = min(total, jobs[0].max_gpus)
            curs[0] = g
            yield iters[0] * jobs[0].time_per_iter(g)
        else:
            for _ in gen_dist_helper(curs, mins, reqs, total, 0):
                tpis = [jobs[i].time_per_iter(curs[i]) for i in range(n)]
                min_t = INF
                min_idx = -1
                for idx, t in enumerate((iters[i] * tpis[i] for i in range(n))):
                    if t < min_t:
                        min_t = t
                        min_idx = idx

                new_jobs = [jobs[i]
                        for i in range(n) if i != min_idx]
                new_iters = [iters[i] - int(min_t / tpis[i])
                        for i in range(n) if i != min_idx]
                new_mins = [curs[i]
                        for i in range(n) if i != min_idx]

                for jct in gen_dist(new_jobs, [0] * (n-1), total, new_mins, new_iters):
                    yield min_t * n + jct

    share = [0] * len(jobs) 
    curs = [0] * len(jobs)
    min_jct = INF
    for jct in gen_dist(jobs, curs, total_gpus):
        # log('%.1f:%s' % (jct, str(share)), end='\r')
        if jct < min_jct:
            min_jct = jct
            share[:] = curs[:]
    for g, m in zip(share, jobs):
        m.schedule(g)

def srtf_ne(jobs, total_gpus):
    srtf_sorted = sorted(jobs, key=lambda m: m.remain(m.max_gpus))
    gpus = total_gpus
    for m in srtf_sorted:
        if gpus < m.max_gpus:
            m.schedule(0)
        else:
            gpus -= m.max_gpus
            m.schedule(m.max_gpus)

def srsf_ne(jobs, total_gpus):
    srsf_sorted = sorted(jobs, key=lambda m: m.max_gpus * m.remain(m.max_gpus))
    gpus = total_gpus
    for m in srsf_sorted:
        if gpus < m.max_gpus:
            m.schedule(0)
        else:
            gpus -= m.max_gpus
            m.schedule(m.max_gpus)

def optimus(jobs, total_gpus):
    for m in jobs:
        m.gpus = 0

    gpus = total_gpus
    while gpus > 0:
        max_val = 0
        j = None
        for m in jobs:
            if m.gpus == m.max_gpus:
                continue
            val = m.remain(m.gpus) - m.remain(m.gpus + 1)
            if val > max_val:
                max_val = val
                j = m
        if j is None:
            break
        j.gpus += 1
        gpus -= 1

    for m in jobs:
        m.schedule(m.gpus)

def heuristic(jobs, total_gpus):
    remain = INF
    shortest = None
    for i, m in enumerate(jobs):
        r = m.remain(min(m.max_gpus, total_gpus))
        if r < remain:
            shortest = m
            remain = r

    g = min(shortest.max_gpus, total_gpus)
    shortest.schedule(g)
    gpus = total_gpus - g

    js = [j for j in jobs if not j is shortest]

    req_list = [m.max_gpus for m in js]
    alloc_list, _ = round_robin(req_list, gpus)
    for i, m in enumerate(js):
        m.schedule(alloc_list[i])

def max_speedup(jobs, total_gpus):
    js = [m for m in jobs]
    for m in js:
        m.gpus = 0
    gpus = total_gpus
    while gpus > 0 and len(js) > 0:
        cand = js[0]
        for m in js[1:]:
            if m.speedup(m.gpus + 1) - m.speedup(m.gpus) > \
                    cand.speedup(cand.gpus + 1) - cand.speedup(cand.gpus):
                cand = m
        cand.gpus += 1
        if cand.gpus == cand.max_gpus:
            js.remove(cand)
        gpus -= 1

    for m in jobs:
        m.schedule(m.gpus)

def opt_gs(jobs, total_gpus):
    def g(m):
        return (m.speedup(m.gpus + 1) - m.speedup(m.gpus))/m.speedup(m.max_gpus)

    js = [m for m in jobs]
    for m in js:
        m.gpus = 0
    gpus = total_gpus
    while gpus > 0 and len(js) > 0:
        cand = js[0]
        for m in js[1:]:
            if g(m) > g(cand):
                cand = m
        cand.gpus += 1
        if cand.gpus == cand.max_gpus:
            js.remove(cand)
        gpus -= 1

    for m in jobs:
        m.schedule(m.gpus)

def opt_2jobs(jobs, total_gpus):
    js = [m for m in jobs]
    for m in js:
        m.gpus = 0
    gpus = total_gpus
    while gpus > 0 and len(js) > 0:
        cand = js[0]
        for m in js[1:]:
            if m.finish_time() < cand.finish_time():
                l = m
                h = cand
            else:
                l = cand
                h = m
            lg = l.gpus
            hg = h.gpus
            mlg = min(l.max_gpus, total_gpus)
            mhg = min(h.max_gpus, total_gpus)
            if l.remain(lg) < h.remain(hg + 1):
                if (l.throughput(lg)/(l.throughput(lg + 1) - l.throughput(lg))) <= \
                    (h.throughput(hg + 1)/(h.throughput(hg + 1) - h.throughput(hg))):
                    cand = l
                else:
                    cand = h
            elif (1/l.remain(lg + 1) - 1/l.remain(lg)) > (1/h.remain(hg + 1) - 1/h.remain(hg)):
                cand = l
            else:
                cand = h
        cand.gpus += 1
        if cand.gpus == cand.max_gpus:
            js.remove(cand)
        gpus -= 1
    for m in jobs:
        m.schedule(m.gpus)

def opt_tsgs(jobs, total_gpus):
    def g(m):
        return (m.throughput(m.gpus + 1) - m.throughput(m.gpus))/m.throughput(m.max_gpus)
    
    def t0g0(js):
        s = js[0]
        st = s.remain(s.gpus)
        for m in js[1:]:
            mt = m.remain(m.gpus)
            if mt < st:
                s = m
                st = mt
        return st * (len(js) - sum([m.throughput(m.gpus)/m.throughput(m.max_gpus) for m in js]))

    js = [m for m in jobs]
    for m in js:
        m.gpus = 0
    gpus = total_gpus
    while gpus > 0 and len(js) > 0:
        cand = js[0]
        for m in js[1:]:
            if g(m) > g(cand):
                cand = m
        cand.gpus += 1
        if cand.gpus == cand.max_gpus:
            js.remove(cand)
        gpus -= 1

    x = t0g0(jobs)
    for m0, m1 in permutations(jobs, 2):
        if m0.gpus >= m0.max_gpus or m1.gpus <= 0:
            continue
        m0.gpus += 1
        m1.gpus -= 1
        y = t0g0(jobs)
        while y < x:
            # log('%.1f, %s' % (y, str([m.gpus for m in jobs])))
            m0.gpus += 1
            m1.gpus -= 1
            if m0.gpus > m0.max_gpus or m1.gpus < 0:
                break
            x = y
            y = t0g0(jobs)
        m0.gpus -= 1
        m1.gpus += 1

    for m in jobs:
        m.schedule(m.gpus)

def tiresias_las(jobs, total_gpus, thres=2*3600, starving_timeout=None):
    """Tiresias-LAS"""
    gpus = total_gpus
    preempt = []
    no_preempt = []
    for m in jobs:
        if m.running_time * m.gpus >= thres:
            # Put jobs with low priority in preempt
            preempt.append(m)
        elif starving_timeout is None:
            no_preempt.append(m)
        else:
            # Schedule starving jobs
            if m.gpus > 0 or m.next_event_time > m.current_time:
                no_preempt.append(m)
            elif m.max_gpus <= gpus:
                m.schedule(m.max_gpus, thres / m.max_gpus)
                gpus -= m.max_gpus
    # Schedule prior jobs first
    js = sorted(no_preempt, key=lambda m: m.init_sched_time) + \
            sorted(preempt, key=lambda m: m.init_sched_time)
    for m in js:
        if m.max_gpus <= gpus:
            m.schedule(m.max_gpus, thres / m.max_gpus)
            gpus -= m.max_gpus
            log('SET TIMEOUT (%s): %.1f' % (m.name, m.next_event_time))
        elif starving_timeout is None:
            m.schedule(0)
        else:
            m.schedule(0, starving_timeout)
            log('SET TIMEOUT (%s): %.1f' % (m.name, m.next_event_time))