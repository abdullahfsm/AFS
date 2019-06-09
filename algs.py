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

def argmax(seq):
    val = -INF
    idx = None
    for i, v in enumerate(seq):
        if v > val:
            val = v
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
        t = remain * m.time_per_iter(share[j])
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
        t = remain * m.time_per_iter(share[j])
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
                max_gain = fac * (1 - j.throughput(r) / j.throughput(r + 1))
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
                gain = facs[k] * (j.throughput(r + 1) - j.throughput(r)) / j.throughput(rmap[k][0])
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
                key=lambda m: remain_dict[m] * m.time_per_iter(gpus_dict[m][-1]))
        order.append(js[idx])
        del js[idx]
        for m in js:
            remain_dict[m] -= int(t / m.time_per_iter(gpus_dict[m][-1]))
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

def brute_force_ne(jobs, total_gpus, state):
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
    if not jobs[-1].just_arrived:
        # jobs finished
        n = len(jobs)
        del state[0][:-n]
        del state[1][:-n]
        for g, j in zip(state[0][0], state[1]):
            j.schedule(g)
        # try:
        #     log('%d,%f' % (j.current_time, calc_sum_jct(state[1], state[0])))
        # except:
        #     raise Exception('Invalid share:\n%s\n%s' % (str(state[1]), str(state[0])))
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
    for x in range(len(jobs)):
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
    state[0] = shares
    state[1] = js

def srtf_ne(jobs, total_gpus, state):
    srtf_sorted = sorted(jobs, key=lambda m: m.remain(m.max_gpus))
    gpus = total_gpus
    for m in srtf_sorted:
        if gpus < m.max_gpus:
            m.schedule(0)
        else:
            gpus -= m.max_gpus
            m.schedule(m.max_gpus)

def srsf_ne(jobs, total_gpus, state):
    srsf_sorted = sorted(jobs, key=lambda m: m.max_gpus * m.remain(m.max_gpus))
    gpus = total_gpus
    for m in srsf_sorted:
        if gpus < m.max_gpus:
            m.schedule(0)
        else:
            gpus -= m.max_gpus
            m.schedule(m.max_gpus)

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

def heuristic(jobs, total_gpus, state):
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

def opt_gs(jobs, total_gpus, state):
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
                key=lambda m: remain_dict[m] * m.time_per_iter(gpus_dict[m][-1]))
        order.append(js[idx])
        del js[idx]
        for m in js:
            remain_dict[m] -= int(t / m.time_per_iter(gpus_dict[m][-1]))
    shares = []
    for i in range(len(jobs)):
        shares.append([gpus_dict[m][i] for m in order[i:]])
    log('%d,%f' % (jobs[0].current_time, calc_sum_jct(order, shares)))
    for g, m in zip(shares[0], order):
        m.schedule(g)

def opt_2jobs(jobs, total_gpus, state):
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

def opt_tsgs_new(jobs, total_gpus, state):
    def g(m):
        return 1 - m.throughput(m.gpus)/m.throughput(m.max_gpus)

    def remain(m, s):
        sr = s.remain(s.gpus)
        int(sr)
        it = m.remain_iter - int(sr / m.time_per_iter(m.gpus))
        return sr + it / m.throughput(m.max_gpus)

    gpus = 0
    min_m = None
    min_r = INF
    for m in jobs:
        m.gpus = m.max_gpus
        gpus += m.max_gpus
        r = m.remain(m.gpus - 1) - m.remain(m.gpus)
        if r < min_r:
            min_m = m
            min_r = r

    if gpus <= total_gpus + 1:
        if gpus == total_gpus + 1:
            min_m.gpus -= 1
            gpus -= 1
        for m in jobs:
            m.schedule(m.gpus)
        return

    min_r = INF
    min_m = None
    for m in jobs:
        r = m.remain(m.gpus)
        if r < min_r:
            min_r = r
            min_m = m
    js = sorted(jobs, key=lambda m: remain(m, min_m))

    while gpus > total_gpus:
        costs = []
        #
        s = js[0]
        remains = [remain(m, s) for m in js]
        sr = remains[0]
        diff = s.remain(s.gpus - 1) - sr
        cost = diff
        for i in range(1, len(js)):
            u = js[i]
            ur = remains[i]
            d = diff * g(u)
            d = min(ur + d, u.remain(u.gpus)) - ur
            cost += d
        costs.append(cost)
        for k in range(1, len(js)):
            j = js[k]
            diff = sr * (j.throughput(j.gpus) - j.throughput(j.gpus - 1)) / j.throughput(j.max_gpus)
            cost = diff
            for i in range(k + 1, len(js)):
                u = js[i]
                ur = remains[i]
                d = diff * g(u)
                d = min(ur + d, u.remain(u.gpus)) - ur
                cost += d
            costs.append(cost)

        for i, c in sorted(enumerate(costs), key=lambda t: t[1]):
            if js[i].gpus > 0:
                js[i].gpus -= 1
                break
        gpus -= 1
        min_r = INF
        min_m = None
        for m in jobs:
            r = m.remain(m.gpus)
            if r < min_r:
                min_r = r
                min_m = m
        js = sorted(js, key=lambda m: remain(m, min_m))

    for m in jobs:
        m.schedule(m.gpus)

def opt_tsgs(jobs, total_gpus, state):
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