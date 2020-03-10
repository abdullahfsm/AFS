import sys
from itertools import permutations

INF = float('inf')

def log(msg, end='\n'):
    sys.stderr.write('%s%s' % (str(msg), end))

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

def argmax(seq, key=None):
    val = -INF
    idx = None
    if key is None:
        for i, v in enumerate(seq):
            if v > val:
                val = v
                idx = i
    else:
        for i, v in enumerate(seq):
            this_val = key(v)
            if this_val > val:
                val = this_val
                idx = i
    return idx, val

def argmin(seq, key=None):
    val = INF
    idx = None
    if key is None:
        for i, v in enumerate(seq):
            if v < val:
                val = v
                idx = i
    else:
        for i, v in enumerate(seq):
            this_val = key(v)
            if this_val < val:
                val = this_val
                idx = i
    return idx, val

def jct_factor(pmap):
    """
      Args:
        pmap:  2D list of p_(job;slot). E.g.
                [[p_00, p_10, p_20],
                 [      p_11, p_21],
                 [            p_22]]
    """
    n = len(pmap[0])
    f = 1
    jfs = [1]
    for j in range(1, n):
        # jp: list of p_(job;slot) of job j. E.g. [p_20, p_21, p_22].
        jp = [pmap[s][j - n] for s in range(j + 1)]
        jf = 0
        for i in range(j):
            jf += jfs[i] * (jp[i + 1] - jp[i])
        jf /= jp[-1]
        f += jf
        jfs.append(jf)
    return f

def calc_jcts(js, shares):
    n = len(js)
    jct = js[0].remain(shares[0][0])
    ts = [jct]
    jcts = [jct]
    for j in range(1, n):
        # share: list of share of job j.
        m = js[j]
        share = [shares[s][j - n] for s in range(j + 1)]
        jct = 0
        remain = m.remain_iter
        for i in range(j):
            jct += ts[i]
            remain -= int(ts[i] * m.throughput(share[i]))
        t = remain * m.tpi(share[j])
        jct += t
        jcts.append(jct)
        ts.append(t)
    return jcts

def calc_sum_jct(js, shares):
    n = len(js)
    sum_jct = js[0].remain(shares[0][0])
    ts = [sum_jct]
    for j in range(1, n):
        # share: list of share of job j.
        m = js[j]
        share = [shares[s][j - n] for s in range(j + 1)]
        jct = 0
        remain = m.remain_iter
        for i in range(j):
            jct += ts[i]
            remain -= int(ts[i] * m.throughput(share[i]))
        t = remain * m.tpi(share[j])
        jct += t
        sum_jct += jct
        ts.append(t)
    return sum_jct

def opt_r(js, total_gpus):
    """
      Args:
        js: List of jobs in finishing order.
    """
    n = len(js)
    rmap = [[1] + [0] * i for i in range(n - 1, 0, -1)]
    rmap.append([min(js[-1].max_gpus, total_gpus)])
    pmap = [[js[n - i - 1].throughput(1)] + [0] * i for i in range(n - 1, 0, -1)]
    pmap.append([js[-1].throughput(min(js[-1].max_gpus, total_gpus))])
    facs = [0] * (n - 1)
    facs.append(1)
    # Optimize rmap
    for i in range(n - 2, -1, -1):
        # Start from the longest job to the shortest one
        fac = jct_factor(pmap[i:])
        gpus = 1
        while gpus < total_gpus:
            # Compare gain of each job and get the max one
            j = js[i]
            r = rmap[i][0]
            # print(rmap, end=',')
            if r < j.max_gpus:
                max_gain = fac * (1 - j.throughput(r) * j.tpi(r + 1))
                max_k = i
                # rmap[i][0] += 1
                # print('JCT(%s) %.1f, ' % (str(rmap), calc_sum_jct(js, rmap)), end='')
                # rmap[i][0] -= 1
            else:
                max_gain = -1
                max_k = None
            # print('%.4f' % max_gain, end=',')
            for k in range(i + 1, n):
                if rmap[i + 1][k - i - 1] == 0:
                    continue
                j = js[k]
                r = rmap[i][k - i]
                if r >= j.max_gpus:
                    continue
                gain = facs[k] * (j.throughput(r + 1) - j.throughput(r)) * j.tpi(rmap[k][0])
                if gain > max_gain:
                    max_gain = gain
                    max_k = k
                # rmap[i][k - i] += 1
                # print('JCT(%s) %.1f, ' % (str(rmap), calc_sum_jct(js, rmap)), end='')
                # rmap[i][k - i] -= 1
                # print('%.4f' % gain, end=',')
            if max_k is None:
                # print('')
                break
            # Give one more GPU to the max one
            rmap[i][max_k - i] += 1
            p_old = pmap[i][max_k - i]
            p_new = js[max_k].throughput(rmap[i][max_k - i])
            pmap[i][max_k - i] = p_new
            if max_k != i:
                # Update fac
                fac -= (p_new - p_old) / pmap[max_k][0]
            # print('AvgJCT: %.1f' % calc_sum_jct(js, rmap))
            gpus += 1
        # Store fac
        facs[i] = fac
    # Validate
    for i in range(n):
        for j in range(i + 1):
            assert(rmap[j][i - j] <= js[i].max_gpus)
    # Return list of GPU share of each slot
    return rmap

################################################################################

def max_min_test(jobs, total_gpus, state):
    remain_dict = {m: m.remain_iter for m in jobs}
    gpus_dict = {m: [] for m in jobs}
    js = [m for m in jobs]
    order = []
    while len(js) > 0:
        share, _ = round_robin([m.max_gpus for m in js], total_gpus)
        for g, m in zip(share, js):
            gpus_dict[m].append(g)
        idx, t = argmin(js,
                key=lambda m: remain_dict[m] * m.tpi(gpus_dict[m][-1]))
        order.append(js[idx])
        del js[idx]
        for m in js:
            remain_dict[m] -= int(t / m.tpi(gpus_dict[m][-1]))
    shares = []
    for i in range(len(jobs)):
        shares.append([gpus_dict[m][i] for m in order[i:]])
    log('%d,%f' % (jobs[0].current_time, calc_sum_jct(order, shares)))
    for g, m in zip(shares[0], order):
        m.schedule(g)

def max_min(jobs, total_gpus, state):
    req_list = [m.max_gpus for m in jobs]
    alloc_list, _ = round_robin(req_list, total_gpus)
    for i, m in enumerate(jobs):
        m.schedule(alloc_list[i])

def brute_force(jobs, total_gpus, state):
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
            yield iters[0] * jobs[0].tpi(g)
        else:
            for _ in gen_dist_helper(curs, mins, reqs, total, 0):
                tpis = [jobs[i].tpi(curs[i]) for i in range(n)]
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

def opt_greedy(jobs, total_gpus, state):
    num_jobs = len(jobs)
    min_sum_jct = INF
    min_js = None
    min_share = None
    for js in permutations(jobs):
        shares = opt_r(js, total_gpus)
        sum_jct = calc_sum_jct(js, shares)
        # print(js, shares[0], sum_jct/num_jobs/3600)
        if sum_jct < min_sum_jct:
            min_sum_jct = sum_jct
            min_js = js
            min_share = shares[0]

    for i, m in enumerate(min_js):
        m.schedule(min_share[i])

def opt_boundary(jobs, total_gpus, state):
    # if not jobs[-1].just_arrived:
    #     # jobs finished
    #     n = len(jobs)
    #     del state[0][:-n]
    #     del state[1][:-n]
    #     for g, j in zip(state[0][0], state[1]):
    #         j.schedule(g)
    #     # try:
    #     #     log('%d,%f' % (j.current_time, calc_sum_jct(state[1], state[0])))
    #     # except:
    #     #     raise Exception('Invalid share:\n%s\n%s' % (str(state[1]), str(state[0])))
    #     return
    if sum([m.max_gpus for m in jobs]) <= total_gpus:
        for m in jobs:
            m.schedule(m.max_gpus)
        return

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

    js = sorted(jobs, key=lambda m: m.remain(m.gpus))
    shares = opt_r(js, total_gpus)
    for x in range(3):
        jcts = calc_jcts(js, shares)
        jcts, new_js = zip(*sorted(zip(jcts, js), key=lambda t: t[0]))
        is_equal = True
        for new, old in zip(new_js, js):
            if not new is old:
                is_equal = False
                break
        js = list(new_js)
        if is_equal:
            break
        shares = opt_r(js, total_gpus)

    share = shares[0]
    # log('%d,%f' % (js[0].current_time, sum(jcts)))

    for i, m in enumerate(js):
        m.schedule(share[i])
    # state[0] = shares
    # state[1] = js

def fifo(jobs, total_gpus, state):
    fifo_sorted = sorted(jobs, key=lambda m: m.arrival_time)
    gpus = total_gpus
    for m in fifo_sorted:
        if gpus < m.philly_request:
            m.schedule(0)
        else:
            gpus -= m.philly_request
            m.schedule(m.philly_request)

def srtf(jobs, total_gpus, state):
    srtf_sorted = sorted(jobs, key=lambda m: m.remain(m.philly_request))
    gpus = total_gpus
    for m in srtf_sorted:
        if gpus < m.philly_request:
            m.schedule(0)
        else:
            gpus -= m.philly_request
            m.schedule(m.philly_request)

def srsf(jobs, total_gpus, state):
    srsf_sorted = sorted(jobs, key=lambda m: m.philly_request * m.remain(m.philly_request))
    gpus = total_gpus
    for m in srsf_sorted:
        if gpus < m.philly_request:
            m.schedule(0)
        else:
            gpus -= m.philly_request
            m.schedule(m.philly_request)

def fifo_relaxed(jobs, total_gpus, state):
    fifo_sorted = sorted(jobs, key=lambda m: m.arrival_time)
    gpus = total_gpus
    for m in fifo_sorted:
        if gpus < m.philly_request:
            m.schedule(0)
        else:
            gpus -= m.philly_request
            m.schedule(m.philly_request)
    for m in fifo_sorted:
        if m.gpus != 0:
            continue
        if gpus == 0:
            break
        g = min(gpus, m.philly_request)
        gpus -= g
        m.schedule(g)

def srtf_relaxed(jobs, total_gpus, state):
    srtf_sorted = sorted(jobs, key=lambda m: m.remain(m.philly_request))
    gpus = total_gpus
    for m in srtf_sorted:
        if gpus < m.philly_request:
            m.schedule(0)
        else:
            gpus -= m.philly_request
            m.schedule(m.philly_request)
    for m in srtf_sorted:
        if m.gpus != 0:
            continue
        if gpus == 0:
            break
        g = min(gpus, m.philly_request)
        gpus -= g
        m.schedule(g)

def srsf_relaxed(jobs, total_gpus, state):
    srsf_sorted = sorted(jobs, key=lambda m: m.philly_request * m.remain(m.philly_request))
    gpus = total_gpus
    for m in srsf_sorted:
        if gpus < m.philly_request:
            m.schedule(0)
        else:
            gpus -= m.philly_request
            m.schedule(m.philly_request)
    for m in srsf_sorted:
        if m.gpus != 0:
            continue
        if gpus == 0:
            break
        g = min(gpus, m.philly_request)
        gpus -= g
        m.schedule(g)

def optimus(jobs, total_gpus, state):
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

def max_speedup(jobs, total_gpus, state):
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

def opt_2jobs_helper(jobs, total_gpus):
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
    return [m.gpus for m in jobs]

def opt_2jobs_test(jobs, total_gpus, state):
    remain_dict = {m: m.remain_iter for m in jobs}
    gpus_dict = {m: [] for m in jobs}
    js = [m for m in jobs]
    order = []
    while len(js) > 0:
        share = opt_2jobs_helper(js, total_gpus)
        for g, m in zip(share, js):
            gpus_dict[m].append(g)
        idx, t = argmin(js,
                key=lambda m: remain_dict[m] * m.tpi(gpus_dict[m][-1]))
        order.append(js[idx])
        del js[idx]
        for m in js:
            remain_dict[m] -= int(t / m.tpi(gpus_dict[m][-1]))
    shares = []
    for i in range(len(jobs)):
        shares.append([gpus_dict[m][i] for m in order[i:]])
    log('%d,%f' % (jobs[0].current_time, calc_sum_jct(order, shares)))
    for g, m in zip(shares[0], order):
        m.schedule(g)

def alg_c(jobs, total_gpus, state):
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
                if l.throughput(lg) * l.rdp(lg) <= h.throughput(hg+1) * h.rdp(hg):
                    cand = l
                else:
                    cand = h
            elif l.dp(lg)/l.remain_iter > h.dp(hg)/h.remain_iter:
                cand = l
            else:
                cand = h
        cand.gpus += 1
        if cand.gpus == cand.max_gpus:
            js.remove(cand)
        gpus -= 1
    for m in jobs:
        m.schedule(m.gpus)

def alg_c_eq(jobs, total_gpus, state):
    js = [m for m in jobs]
    for m in js:
        m.gpus = 0
    gpus = total_gpus
    while gpus > 0 and len(js) > 0:
        cand = js[0]
        for m in js[1:]:
            if m.remain(m.gpus) < cand.remain(cand.gpus):
                l, h = m, cand
            else:
                l, h = cand, m
            sl0 = 1 / l.remain(l.gpus)
            sl1 = 1 / l.remain(l.gpus + 1)
            sh0 = 1 / h.remain(h.gpus)
            sh1 = 1 / h.remain(h.gpus + 1)
            if sl0 == 0:
                cand = l if sl1 > sh1 else h
            elif (sl1 - sl0) / sl0 > (sh1 - sh0) / sh1:
                cand = l
            else:
                cand = h
        cand.gpus += 1
        if cand.gpus == cand.max_gpus:
            js.remove(cand)
        gpus -= 1
    for m in jobs:
        m.schedule(m.gpus)

def alg_c_eq2(jobs, total_gpus, state):
    js = [m for m in jobs]
    for m in js:
        m.gpus = 0
    gpus = total_gpus
    while gpus > 0 and len(js) > 0:
        cand = js[0]
        for m in js[1:]:
            if m.remain(m.gpus) < cand.remain(cand.gpus):
                l, h = m, cand
            else:
                l, h = cand, m
            sl0 = 1 / l.remain(l.gpus)
            sl1 = 1 / l.remain(l.gpus + 1)
            sh0 = 1 / h.remain(h.gpus)
            sh1 = 1 / h.remain(h.gpus + 1)
            if sl0 == 0:
                cand = l if sl1 > sh1 else h
            elif sh0 == 0:
                cand = h
            elif (sl1 - sl0) / sl0 >= (sh1 - sh0) / sh0:
                cand = l
            else:
                cand = h
        cand.gpus += 1
        if cand.gpus == cand.max_gpus:
            js.remove(cand)
        gpus -= 1
    for m in jobs:
        m.schedule(m.gpus)

def alg_c_rough(jobs, total_gpus, state):
    js = [m for m in jobs]
    for m in js:
        m.gpus = 0
    gpus = total_gpus
    while gpus > 0 and len(js) > 0:
        cand = js[0]
        for m in js[1:]:
            if m.remain(m.gpus) < cand.remain(cand.gpus):
                l, h = m, cand
            else:
                l, h = cand, m
            if l.gpus == 0:
                cand = l if h.remain(h.gpus + 1) > l.remain(l.gpus + 1) else h
            elif l.gpus <= h.gpus:
                cand = l
            else:
                cand = h
        cand.gpus += 1
        if cand.gpus == cand.max_gpus:
            js.remove(cand)
        gpus -= 1
    for m in jobs:
        m.schedule(m.gpus)

def opt_pp(jobs, total_gpus, state):
    def fac(m):
        return m.throughput(m.gpus + 1) * m.rdp(m.gpus)

    js = [m for m in jobs]
    for m in js:
        m.gpus = 0
    gpus = total_gpus
    while gpus > 0 and len(js) > 0:
        cand = js[0]
        for m in js[1:]:
            if fac(m) <= fac(cand):
                cand = m
        cand.gpus += 1
        if cand.gpus == cand.max_gpus:
            js.remove(cand)
        gpus -= 1

    for m in jobs:
        m.schedule(m.gpus)

def opt_pp_2(jobs, total_gpus, state):
    def fac(m):
        return m.throughput(m.gpus + 1) * m.rdp(m.gpus)

    js = [m for m in jobs]
    for m in js:
        m.gpus = 0
    gpus = total_gpus
    for m in js:
        if gpus > 0:
            m.gpus = 1
            gpus -= 1
        else:
            break
    if gpus > 0:
        while gpus > 0 and len(js) > 0:
            cand = js[0]
            for m in js[1:]:
                if fac(m) <= fac(cand):
                    cand = m
            cand.gpus += 1
            if cand.gpus == cand.max_gpus:
                js.remove(cand)
            gpus -= 1

    for m in jobs:
        m.schedule(m.gpus)

def tiresias_las(jobs, total_gpus, state, thres=3200, starvation_knob=None, relaxed=False):
    """Tiresias-LAS"""
    gpus = total_gpus
    neg_pri = []
    zero_pri = []
    pos_pri = []
    for m in jobs:
        # print(m.current_time, m.preempted_time, m.evicted_time)
        if (m.current_time - m.preempted_time) * m.gpus >= thres:
            # Put jobs with low priority in preempt
            neg_pri.append(m)
        elif starvation_knob is None:
            zero_pri.append(m)
        elif starvation_knob is not None and m.gpus == 0 and m.next_event_time <= m.current_time:
            # Schedule starving jobs
            pos_pri.append(m)
        else:
            zero_pri.append(m)
    # Schedule prior jobs first
    js = sorted(pos_pri, key=lambda m: m.evicted_time) + \
            sorted(zero_pri, key=lambda m: m.init_sched_time) + \
            sorted(neg_pri, key=lambda m: m.init_sched_time)
    for m in js:
        if relaxed and gpus > 0:
            num = min(m.philly_request, gpus)
            m.schedule(num, thres / num)
            gpus -= num
            # log('SET TIMEOUT (%s): %.1f' % (m.name, m.next_event_time))
        elif m.philly_request <= gpus:
            m.schedule(m.philly_request, thres / m.philly_request)
            gpus -= m.philly_request
            # log('SET TIMEOUT (%s): %.1f' % (m.name, m.next_event_time))
        elif starvation_knob is None:
            m.schedule(0)
        elif m.preempted_time == INF:
            assert(m.tiresias_tj != 0)
            m.schedule(0, m.tiresias_tj * starvation_knob)
        else:
            m.schedule(0, (m.current_time - m.preempted_time) * starvation_knob)
            # log('SET TIMEOUT (%s): %.1f' % (m.name, m.next_event_time))

def tiresias_1(jobs, total_gpus, state):
    tiresias_las(jobs, total_gpus, state, thres=1*3600, starvation_knob=2, relaxed=False)

def tiresias_2(jobs, total_gpus, state):
    tiresias_las(jobs, total_gpus, state, thres=2*3600, starvation_knob=2, relaxed=False)

def tiresias_5(jobs, total_gpus, state):
    tiresias_las(jobs, total_gpus, state, thres=5*3600, starvation_knob=2, relaxed=False)

def tiresias_10(jobs, total_gpus, state):
    tiresias_las(jobs, total_gpus, state, thres=10*3600, starvation_knob=2, relaxed=False)

def tiresias_1_starve(jobs, total_gpus, state):
    tiresias_las(jobs, total_gpus, state, thres=1*3600, starvation_knob=None, relaxed=False)

def tiresias_2_starve(jobs, total_gpus, state):
    tiresias_las(jobs, total_gpus, state, thres=2*3600, starvation_knob=None, relaxed=False)

def tiresias_5_starve(jobs, total_gpus, state):
    tiresias_las(jobs, total_gpus, state, thres=5*3600, starvation_knob=None, relaxed=False)

def tiresias_10_starve(jobs, total_gpus, state):
    tiresias_las(jobs, total_gpus, state, thres=10*3600, starvation_knob=None, relaxed=False)

def tiresias_las_relaxed(jobs, total_gpus, state):
    tiresias_las(jobs, total_gpus, state, relaxed=True)