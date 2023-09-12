import sys
import random

INF = float('inf')

SCALE = 1

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

def fifo(jobs, total_gpus):
    fifo_sorted = sorted(jobs, key=lambda m: (m.ts_scheduled, m.ts_arrival))
    gpus = total_gpus
    for m in fifo_sorted:
        if gpus < m.max_gpus:
            m.schedule(0)
        else:
            gpus -= m.max_gpus
            m.schedule(m.max_gpus)

def fifo_elastic(jobs, total_gpus):
    fifo_sorted = sorted(jobs, key=lambda m: (m.ts_scheduled, m.ts_arrival))
    gpus = total_gpus
    for m in fifo_sorted:

        allocation = min(m.max_gpus, gpus)
        m.schedule(allocation)
        gpus -= allocation

def srtf(jobs, total_gpus):
    srtf_sorted = sorted(jobs, key=lambda m: m.exp_remain_time(m.max_gpus))
    gpus = total_gpus
    for m in srtf_sorted:
        if gpus < m.max_gpus:
            m.schedule(0)
        else:
            gpus -= m.max_gpus
            m.schedule(m.max_gpus)

def srsf(jobs, total_gpus):
    srsf_sorted = sorted(jobs, key=lambda m: m.max_gpus * m.exp_remain_time(m.max_gpus))
    gpus = total_gpus
    for m in srsf_sorted:
        if gpus < m.max_gpus:
            m.schedule(0)
        else:
            gpus -= m.max_gpus
            m.schedule(m.max_gpus)

def srsf_elastic(jobs, total_gpus):
    srsf_sorted = sorted(jobs, key=lambda m: m.max_gpus * m.exp_remain_time(m.max_gpus))
    gpus = total_gpus
    for m in srsf_sorted:

        allocation = min(m.max_gpus, gpus)
        m.schedule(allocation)
        gpus -= allocation
        
def optimus(jobs, total_gpus):
    for m in jobs:
        m.tmp_gpus = 0

    gpus = total_gpus
    while gpus > 0:
        max_val = 0
        j = None
        for m in jobs:
            if m.tmp_gpus == m.max_gpus:
                continue
            val = m.exp_remain_time(m.tmp_gpus) - m.exp_remain_time(m.tmp_gpus + 1)
            if val > max_val:
                max_val = val
                j = m
        if j is None:
            break
        j.tmp_gpus += 1
        gpus -= 1

    for m in jobs:
        m.schedule(m.tmp_gpus)

def max_min(jobs, total_gpus):
    js = sorted(jobs, key=lambda m: (m.ts_scheduled, m.ts_arrival))
    req_list = [m.max_gpus for m in js]
    alloc_list, _ = round_robin(req_list, total_gpus)
    for i, m in enumerate(js):
        m.schedule(alloc_list[i])

def alg_c_concept(jobs, total_gpus):
    js = [m for m in jobs]
    for m in js:
        m.tmp_gpus = 0
    gpus = total_gpus
    while gpus > 0 and len(js) > 0:
        cand = js[0]
        for m in js[1:]:
            if m.exp_remain_time(m.tmp_gpus) < cand.exp_remain_time(cand.tmp_gpus):
                l, h = m, cand
            else:
                l, h = cand, m
            sl0 = 1 / l.exp_remain_time(l.tmp_gpus)
            sl1 = 1 / l.exp_remain_time(l.tmp_gpus + 1)
            sh0 = 1 / h.exp_remain_time(h.tmp_gpus)
            sh1 = 1 / h.exp_remain_time(h.tmp_gpus + 1)
            if sl0 == 0:
                cand = l if sl1 > sh1 else h
            elif (sl1 - sl0) / sl0 > (sh1 - sh0) / sh1:
                cand = l
            else:
                cand = h
        cand.tmp_gpus += 1
        if cand.tmp_gpus == cand.max_gpus:
            js.remove(cand)
        gpus -= 1
    for m in jobs:
        m.schedule(m.tmp_gpus)

def alg_c(jobs, total_gpus):
    diff = total_gpus - len(jobs)
    if diff < 0:
        gpus = total_gpus
        for j in sorted(jobs, key=lambda j: j.exp_remain_time(1)):
            if gpus > 0:
                j.schedule(1)
                gpus -= 1
            else:
                j.schedule(0)
    elif diff == 0:
        for j in jobs:
            j.schedule(1)
    else:
        for j in jobs:
            j.tmp_gpus = 1
        js = [j for j in jobs if j.max_gpus > 1]
        while diff > 0 and len(js) > 0:
            cand = js[0]
            for m in js[1:]:
                rm0 = m.exp_remain_time(m.tmp_gpus)
                rc0 = cand.exp_remain_time(cand.tmp_gpus)
                if rm0 < rc0:
                    l, h = m, cand
                    rl0, rh0 = rm0, rc0
                else:
                    l, h = cand, m
                    rl0, rh0 = rc0, rm0
                rl1 = l.exp_remain_time(l.tmp_gpus + 1)
                rh1 = h.exp_remain_time(h.tmp_gpus + 1)
                if rl0 / rl1 + rh1 / rh0 > 2:
                    cand = l
                else:
                    cand = h
            cand.tmp_gpus += 1
            if cand.tmp_gpus == cand.max_gpus:
                js.remove(cand)
            diff -= 1
        for j in jobs:
            j.schedule(j.tmp_gpus)

def lrr_p_helper(jobs, total_gpus):
    def fac1(m):
        return m.throughput(m.tmp_gpus) * m.rdp(m.tmp_gpus)
    def fac2(m):
        return m.throughput(m.tmp_gpus + 1) * m.rdp(m.tmp_gpus)

    for j in jobs[:total_gpus]:
        j.tmp_gpus = 1
    gpus = total_gpus - len(jobs)
    if gpus > 0:
        js = [j for j in jobs if j.max_gpus > 1]
        while gpus > 0 and len(js) > 0:
            cand = js[0]
            for m in js[1:]:
                if fac2(m) <= fac1(cand):
                    cand = m
                elif fac2(cand) > fac1(m):
                    cand = random.choice([cand, m])
                # else:
                #     cand = m
            cand.tmp_gpus += 1
            if cand.tmp_gpus == cand.max_gpus:
                js.remove(cand)
            gpus -= 1
    elif gpus < 0:
        for j in jobs[total_gpus:]:
            j.tmp_gpus = 0

    for m in jobs:
        asdf = m.gpus
        if m.tmp_gpus == 0:
            m.schedule(0)
        else:
            m.schedule(m.tmp_gpus, m.ts_current + 2 * 3600 * SCALE)

def lrr_s_helper(jobs, total_gpus):
    for j in jobs[:total_gpus]:
        j.tmp_gpus = 1
    gpus = total_gpus - len(jobs)
    if gpus > 0:
        js = [j for j in jobs if j.max_gpus > 1]
        while gpus > 0 and len(js) > 0:
            cand = js[0]
            for m in js[1:]:
                if cand.tmp_gpus > m.tmp_gpus:
                    cand = m
            cand.tmp_gpus += 1
            if cand.tmp_gpus == cand.max_gpus:
                js.remove(cand)
            gpus -= 1
    elif gpus < 0:
        for j in jobs[total_gpus:]:
            j.tmp_gpus = 0

    for m in jobs:
        asdf = m.gpus
        if m.tmp_gpus == 0:
            m.schedule(0)
        else:
            m.schedule(m.tmp_gpus, m.ts_current + 2 * 3600 * SCALE)

def lrr_p(jobs, total_gpus):
    keep_promoted = []
    others = []
    if len(jobs) < total_gpus:
        others = jobs
    else:
        for j in jobs:
            if j.ts_scheduled != INF:
                if j.ts_next_event > j.ts_current:
                    keep_promoted.append(j)
                else:
                    j.optpp_sched_cnt += 1
                    others.append(j)
            else:
                others.append(j)
    gpus = total_gpus
    for j in keep_promoted:
        j.schedule(j.gpus, j.ts_next_event)
        gpus -= j.gpus
    if gpus > 0:
        others.sort(key=lambda j: (j.optpp_sched_cnt, j.ts_init_scheduled, j.ts_arrival))
    lrr_p_helper(others, gpus)

def lrr_s(jobs, total_gpus):
    keep_promoted = []
    others = []
    if len(jobs) < total_gpus:
        others = jobs
    else:
        for j in jobs:
            if j.ts_scheduled != INF:
                if j.ts_next_event > j.ts_current:
                    keep_promoted.append(j)
                else:
                    j.optpp_sched_cnt += 1
                    others.append(j)
            else:
                others.append(j)
    gpus = total_gpus
    for j in keep_promoted:
        j.schedule(j.gpus, j.ts_next_event)
        gpus -= j.gpus
    if gpus > 0:
        others.sort(key=lambda j: (j.optpp_sched_cnt, j.ts_init_scheduled, j.ts_arrival))
    lrr_s_helper(others, gpus)

def opt_r(js, total_gpus):
    """
      Args:
        js: List of jobs in finishing order.
    """
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
                max_gain = fac * (1 - j.throughput(r) * j.times_per_iter(r + 1))
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
                gain = facs[k] * (j.throughput(r + 1) - j.throughput(r)) * j.times_per_iter(rmap[k][0])
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

OPT_BOUNDARY_JOBS = None
OPT_BOUNDARY_SHARES = None

def opt_boundary(jobs, total_gpus):
    def calc_jcts(js, shares):
        n = len(js)
        jct = js[0].exp_remain_time(shares[0][0])
        ts = [jct]
        jcts = [jct]
        for j in range(1, n):
            # share: list of share of job j.
            m = js[j]
            share = [shares[s][j - n] for s in range(j + 1)]
            jct = 0
            remain = m.remain_iters
            for i in range(j):
                jct += ts[i]
                remain -= int(ts[i] * m.throughput(share[i]))
            # assert(remain > 0)
            t = remain * m.times_per_iter(share[j])
            jct += t
            jcts.append(jct)
            ts.append(t)
        return jcts

    global OPT_BOUNDARY_JOBS
    global OPT_BOUNDARY_SHARES

    if sum([m.max_gpus for m in jobs]) <= total_gpus:
        for m in jobs:
            m.schedule(m.max_gpus)
        OPT_BOUNDARY_JOBS = None
        OPT_BOUNDARY_SHARES = None
        return

    if OPT_BOUNDARY_JOBS is not None and set(jobs) == set(OPT_BOUNDARY_JOBS[1:]):
        del OPT_BOUNDARY_SHARES[0]
        del OPT_BOUNDARY_JOBS[0]
        for s, j in zip(OPT_BOUNDARY_SHARES[0], OPT_BOUNDARY_JOBS):
            j.schedule(s)
        # log(', '.join(['%d:%d' % (j.jid, j.gpus) for j in OPT_BOUNDARY_JOBS]))
        # log(', '.join(['%d:%.3f' % (j.jid, j.exp_remain_time(j.gpus)) for j in OPT_BOUNDARY_JOBS]))
        # log(', '.join(['%d:%.3f' % (j.jid, j.ts_current) for j in OPT_BOUNDARY_JOBS]))
        # log(', '.join(['%d:%.3f' % (j.jid, j.ts_exp_fin) for j in OPT_BOUNDARY_JOBS]))
        return

    for m in jobs:
        m.tmp_gpus = 0

    gpus = total_gpus
    while gpus > 0:
        max_val = 0
        j = None
        for m in jobs:
            if m.tmp_gpus == m.max_gpus:
                continue
            val = m.exp_remain_time(m.tmp_gpus) - m.exp_remain_time(m.tmp_gpus + 1)
            if val > max_val:
                max_val = val
                j = m
        if j is None:
            break
        j.tmp_gpus += 1
        gpus -= 1

    js = sorted(jobs, key=lambda m: m.exp_remain_time(m.tmp_gpus))
    shares = opt_r(js, total_gpus)
    for x in range(1):
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
    # for s in shares:
    #     log(s)
    OPT_BOUNDARY_SHARES = shares
    OPT_BOUNDARY_JOBS = js

    for s, m in zip(shares[0], js):
        m.schedule(s)
    # log(', '.join(['%d:%d' % (j.jid, j.gpus) for j in js]))
    # log(jcts)
    # log([m.exp_remain_time(m.gpus) for m in js])

def tiresias_las(jobs, total_gpus, thres=3200, starvation_knob=None, relaxed=False):
    """Tiresias-LAS"""
    thres *= SCALE
    gpus = total_gpus
    neg_pri = []
    zero_pri = []
    pos_pri = []
    for m in jobs:
        # print(m.ts_current, m.ts_scheduled, m.ts_evicted)
        if starvation_knob is not None and (m.gpus == 0 or m.ts_scheduled == INF) and (m.tiresias_starving or m.ts_next_event <= m.ts_current):
            # Schedule starving jobs
            pos_pri.append(m)
        elif m.tiresias_evicted or (m.ts_current - m.ts_scheduled) * m.gpus >= thres:
            # Put jobs with low priority in preempt
            m.tiresias_evicted = True
            neg_pri.append(m)
        else:
            zero_pri.append(m)
    # assert(len(zero_pri) == len(jobs))
    # Schedule prior jobs first
    pos_pri = sorted(pos_pri, key=lambda m: m.ts_evicted)
    zero_pri = sorted(zero_pri, key=lambda m: (m.ts_init_scheduled, m.ts_arrival))
    neg_pri = sorted(neg_pri, key=lambda m: m.ts_init_scheduled)
    js = pos_pri + zero_pri + neg_pri
    # input('')
    for m in js:
        if relaxed and gpus > 0:
            num = min(m.max_gpus, gpus)
            m.tiresias_evicted = False
            m.schedule(num, m.ts_current + (thres + num - 1) / num)
            m.tiresias_starving = False
            gpus -= num
            # log('SET TIMEOUT (%s): %.1f' % (m.name, m.ts_next_event))
        elif m.max_gpus <= gpus:
            if m.gpus == 0 or m.ts_next_event <= m.ts_current:
                m.schedule(m.max_gpus, m.ts_current + (thres + m.max_gpus - 1) / m.max_gpus)
            else:
                m.schedule(m.max_gpus, m.ts_next_event)
            m.tiresias_starving = False
            m.tiresias_evicted = False
            gpus -= m.max_gpus
            # log('SET TIMEOUT (%s): %.1f' % (m.name, m.ts_next_event))
        elif starvation_knob is None:
            m.schedule(0)
        elif m.ts_scheduled == INF:
            if m.ts_init_scheduled == INF:
                # This is a job that never have scheduled before
                m.schedule(0)
            elif m.ts_next_event <= m.ts_current:
                assert(sum([j.max_gpus for j in pos_pri]) > total_gpus)
                m.tiresias_starving = True
                m.schedule(0)
            else:
                m.schedule(0, m.ts_next_event)
            if m.gpus != 0:
                log('%d:%d(%.0f,%.0f,%.0f,%.0f)%d' % (m.jid, m.gpus, m.ts_arrival, m.ts_init_scheduled, m.ts_scheduled, m.ts_next_event, m.remain_iters))
                assert(False)
        else:
            m.schedule(0, m.ts_current + (m.ts_current - m.ts_scheduled) * starvation_knob)
    # log('%d] %s %s' % (js[0].ts_current,
    #     str(['%d:%d(%.0f,%.0f,%.0f,%.0f)%d' % (m.jid, m.gpus, m.ts_arrival, m.ts_init_scheduled, m.ts_scheduled, m.ts_next_event, m.remain_iters) for m in zero_pri]),
    #     str(['%d:%d(%.0f,%.0f,%.0f,%.0f)%d' % (m.jid, m.gpus, m.ts_arrival, m.ts_init_scheduled, m.ts_scheduled, m.ts_next_event, m.remain_iters) for m in neg_pri])))

def tiresias_debug(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=float('inf'), starvation_knob=None, relaxed=False)

def tiresias_debug2(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=3200, starvation_knob=100000, relaxed=False)

def tiresias_01_k1(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.1*3600, starvation_knob=1, relaxed=False)

def tiresias_1_k1(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=1*3600, starvation_knob=1, relaxed=False)

def tiresias_2_k1(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=2*3600, starvation_knob=1, relaxed=False)

def tiresias_5_k1(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=5*3600, starvation_knob=1, relaxed=False)

def tiresias_10_k1(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=10*3600, starvation_knob=1, relaxed=False)

def tiresias_01_k2(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.1*3600, starvation_knob=2, relaxed=False)

def tiresias_1_k2(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=1*3600, starvation_knob=2, relaxed=False)

def tiresias_2_k2(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=2*3600, starvation_knob=2, relaxed=False)

def tiresias_5_k2(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=5*3600, starvation_knob=2, relaxed=False)

def tiresias_10_k2(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=10*3600, starvation_knob=2, relaxed=False)

def tiresias_01_k5(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.1*3600, starvation_knob=5, relaxed=False)

def tiresias_1_k5(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=1*3600, starvation_knob=5, relaxed=False)

def tiresias_2_k5(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=2*3600, starvation_knob=5, relaxed=False)

def tiresias_5_k5(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=5*3600, starvation_knob=5, relaxed=False)

def tiresias_10_k5(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=10*3600, starvation_knob=5, relaxed=False)

def tiresias_01_k10(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.1*3600, starvation_knob=10, relaxed=False)

def tiresias_1_k10(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=1*3600, starvation_knob=10, relaxed=False)

def tiresias_2_k10(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=2*3600, starvation_knob=10, relaxed=False)

def tiresias_2_k100(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=2*3600, starvation_knob=100, relaxed=False)

def tiresias_2_k200(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=2*3600, starvation_knob=200, relaxed=False)

def tiresias_5_k10(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=5*3600, starvation_knob=10, relaxed=False)

def tiresias_5_k200(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=5*3600, starvation_knob=200, relaxed=False)

def tiresias_10_k10(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=10*3600, starvation_knob=10, relaxed=False)

def tiresias_001_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.01*3600, starvation_knob=None, relaxed=False)

def tiresias_002_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.02*3600, starvation_knob=None, relaxed=False)

def tiresias_005_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.05*3600, starvation_knob=None, relaxed=False)

def tiresias_01_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.1*3600, starvation_knob=None, relaxed=False)

def tiresias_02_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.2*3600, starvation_knob=None, relaxed=False)

def tiresias_02_k100(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.2*3600, starvation_knob=100, relaxed=False)

def tiresias_02_k200(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.2*3600, starvation_knob=200, relaxed=False)

def tiresias_02_k500(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.2*3600, starvation_knob=500, relaxed=False)

def tiresias_02_starve_relaxed(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.2*3600, starvation_knob=None, relaxed=True)

def tiresias_05_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=0.5*3600, starvation_knob=None, relaxed=False)

def tiresias_1_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=1*3600, starvation_knob=None, relaxed=False)

def tiresias_2_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=2*3600, starvation_knob=None, relaxed=False)

def tiresias_5_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=5*3600, starvation_knob=None, relaxed=False)

def tiresias_10_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=10*3600, starvation_knob=None, relaxed=False)

def tiresias_20_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=20*3600, starvation_knob=None, relaxed=False)

def tiresias_50_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=50*3600, starvation_knob=None, relaxed=False)

def tiresias_100_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=100*3600, starvation_knob=None, relaxed=False)

def tiresias_100_k200(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=100*3600, starvation_knob=200, relaxed=False)

def tiresias_200_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=200*3600, starvation_knob=None, relaxed=False)

def tiresias_500_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=500*3600, starvation_knob=None, relaxed=False)

def tiresias_1000_starve(jobs, total_gpus):
    tiresias_las(jobs, total_gpus, thres=1000*3600, starvation_knob=None, relaxed=False)


FIFO = fifo
FIFO_ELASTIC = fifo_elastic
Tiresias = tiresias_50_starve
SRTF = srtf
SRSF = srsf
SRSF_ELASTIC = srsf_elastic
Optimus = optimus
MaxMin = max_min
Opt2Jobs = alg_c
OptPP = lrr_p
OptBoundary = opt_boundary