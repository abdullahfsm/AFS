INF = float('inf')

# Scale total iterations of all models.
_SCALE_TOTAL_ITER = 0.1

class Model(object):
    def __init__(self, name, total_iter, times_per_iter):
        # Constants
        self.name = name
        self.arrival_time = 0
        self.total_iter = int(total_iter * _SCALE_TOTAL_ITER)
        self.times_per_iter = times_per_iter
        self.throughputs = [1 / float(t) for t in times_per_iter]
        self.dps = [self.throughputs[0]] + [self.throughputs[i+1] - self.throughputs[i]
            for i in range(len(self.throughputs)-1)]
        self.rdps = [1/dp if dp != 0 else INF for dp in self.dps]
        self.speedups = [times_per_iter[0] / float(t) for t in times_per_iter]

        # Number of iterations remaining
        self.remain_iter = self.total_iter
        # Number of GPUs currently allocated
        self.gpus = 0
        # Current absolute time
        self.current_time = 0
        # The recent absolute time when is alloced zero GPU
        self.evicted_time = 0
        # The recent absolute time when is alloced one or more GPUs
        self.preempted_time = 0
        # How long has this model been evicted since arrival
        self.total_evicted = 0
        self.total_evicted_temp = 0
        # Abs time when the model is initially executed
        self.init_sched_time = INF
        # The nearest abs time when this model raises a re-allocation event.
        self.next_event_time = INF

        # For tests
        self.tickets = []

        # Check validity
        self.validate()

    @property
    def max_gpus(self):
        return len(self.speedups)

    @property
    def is_finished(self):
        return self.remain_iter <= 0

    @property
    def just_arrived(self):
        return self.current_time == self.arrival_time

    @property
    def running_for(self):
        if self.preempted_time == 0:
            return 0
        return self.current_time - self.preempted_time

    @property
    def starving_for(self):
        if self.evicted_time == 0:
            return 0
        return self.current_time - self.evicted_time

    @property
    def total_runtime(self):
        return self.current_time - self.arrival_time

    def submit(self, arrival_time, max_gpus=None, length=None):
        self.arrival_time = arrival_time
        self.current_time = arrival_time
        self.evicted_time = arrival_time
        if max_gpus is not None and max_gpus < self.max_gpus:
            self.times_per_iter = self.times_per_iter[:max_gpus]
            self.throughputs = self.throughputs[:max_gpus]
            self.speedups = self.speedups[:max_gpus]
        if length is not None:
            self.total_iter = int(length / self.times_per_iter[-1])
            if self.total_iter == 0:
                self.total_iter = 1
        self.remain_iter = self.total_iter
        return self

    def tpi(self, num_gpus):
        if num_gpus <= 0:
            return INF
        return self.times_per_iter[num_gpus - 1]

    def throughput(self, num_gpus):
        if num_gpus <= 0:
            return 0
        return self.throughputs[num_gpus - 1]

    def dp(self, num_gpus):
        return self.dps[num_gpus]

    def rdp(self, num_gpus):
        return self.rdps[num_gpus]

    def speedup(self, num_gpus):
        if num_gpus <= 0:
            return -INF
        return self.speedups[num_gpus - 1]

    def remain(self, num_gpus):
        if num_gpus <= 0:
            return INF
        return self.remain_iter * self.times_per_iter[num_gpus - 1]

    def finish_time(self):
        if self.gpus == 0:
            return INF
        return self.current_time + self.remain(self.gpus)

    def schedule(self, num_gpus, timeout=None):
        assert(num_gpus >= 0)
        assert(num_gpus <= self.max_gpus)
        assert(timeout is None or timeout >= 0)
        self.gpus = num_gpus
        fin_time = self.finish_time()
        if timeout is None:
            # Default event time: when this model finishes
            self.next_event_time = fin_time
        else:
            # Set the nearest event only
            self.next_event_time = min(fin_time, self.current_time + timeout)
        # print('schedule %s: %f, %f' % (self.name, fin_time, self.current_time))

    def continue_until(self, time):
        """Progress time until `time`."""
        time_diff = time - self.current_time
        if time_diff < 0:
            raise Exception('cur_time %d, time %d' % (self.current_time, time))
        if time_diff == 0:
            return
        if self.gpus == 0:
            if self.evicted_time == 0:
                self.evicted_time = self.current_time
                self.preempted_time = 0
            self.current_time = time
            self.total_evicted = self.total_evicted_temp + time - self.evicted_time
        else:
            if self.preempted_time == 0:
                self.total_evicted_temp += self.current_time - self.evicted_time
                self.preempted_time = self.current_time
                self.evicted_time = 0
            tpi = self.times_per_iter[self.gpus - 1]
            proced_iter = int(time_diff / float(tpi) + 1e-5)
            if self.remain_iter <= proced_iter:
                # Job finishes
                self.remain_iter = 0
                self.current_time += proced_iter * tpi
            else:
                # Still has remaining iterations
                self.remain_iter -= proced_iter
                if self.remain_iter == 1:
                    self.remain_iter = 0
                self.current_time = time
            if self.init_sched_time == INF:
                self.init_sched_time = time

    def validate(self):
        """Validate if the model meets assumptions of simulation."""
        assert(self.arrival_time >= 0)
        assert(self.total_iter > 0)
        assert(len(self.speedups) > 0)
        assert(self.speedups[0] == 1.)
        if len(self.speedups) == 2:
            assert(self.speedups[0] <= self.speedups[1])
            return
        for i in range(len(self.speedups) - 2):
            # Speedups should be monotonic decreasing, and its gradient also should
            # be monotonic decreasing.
            s0 = self.speedups[i]
            s1 = self.speedups[i + 1]
            s2 = self.speedups[i + 2]
            assert(s0 <= s1)
            assert(s1 <= s2)
            assert(s1 - s0 >= s2 - s1)

    def finish_info(self):
        return '%.1f,%s,%.1f,%.1f' % (self.current_time,
                                      self.name,
                                      self.current_time - self.arrival_time,
                                      self.total_evicted)

################################################################################

class FacenetModel64(Model):
    def __init__(self):
        super(FacenetModel64, self).__init__('FaceNetModel64',
                45000000 // 64,
                # [0.2476, 0.1641, 0.1324, 0.1229])
                [0.2476, 0.1850, 0.1477, 0.1230])
        self.import_graph_time = 8.8713
        self.first_iter_time = 15.8114

class FacenetModel128(Model):
    def __init__(self):
        super(FacenetModel128, self).__init__('FaceNetModel128',
                45000000 // 128,
                [0.4357, 0.2595, 0.1959, 0.1627,
                 0.1484, 0.1403, 0.1363, 0.1284])
        self.import_graph_time = 8.8713
        self.first_iter_time = 15.8114

class FacenetModel256(Model):
    def __init__(self):
        super(FacenetModel256, self).__init__('FaceNetModel256',
                45000000 // 256,
                [0.9000, 0.4499, 0.3235, 0.2614,
                 0.2259, 0.1978, 0.1794, 0.1650,
                 0.1605, 0.1531, 0.1472, 0.1456])
        self.import_graph_time = 8.8713
        self.first_iter_time = 15.8114

class VggnetModel256(Model):
    def __init__(self):
        super(VggnetModel256, self).__init__('VggnetModel256',
                153740040 // 256,
                # [2.8591, 2.1769, 1.4946, 0.8124,
                #  0.7849, 0.7574, 0.7299, 0.7024,
                #  0.6400, 0.5777, 0.5153, 0.4529,
                #  0.4343, 0.4157, 0.3971, 0.3786])
                [2.8591, 1.554, 1.067, 0.8125,
                 0.7351, 0.6712, 0.6176, 0.572,
                 0.5366, 0.5055, 0.4779, 0.4532,
                 0.4317, 0.4124, 0.3948, 0.3787])
        self.import_graph_time = 0.3524
        self.first_iter_time = 3.5694

class GooglenetModel128(Model):
    def __init__(self):
        super(GooglenetModel128, self).__init__('GooglenetModel128',
                153740040 // 128,
                # [0.3631,  0.1908,  0.1384,  0.1074,
                #  0.09246, 0.08308, 0.07820, 0.06242,
                #  0.05980, 0.05287, 0.05127, 0.05008,
                #  0.04694, 0.04701, 0.04521, 0.04169,
                #  0.04169, 0.04169, 0.04115, 0.04095])
                [0.36310, 0.20233, 0.14029, 0.10740,
                 0.09095, 0.07889, 0.06966, 0.06240,
                 0.05870, 0.05543, 0.05251, 0.04990,
                 0.04754, 0.04541, 0.04347, 0.04170,
                 0.04151, 0.04133, 0.04116, 0.04100])
        self.import_graph_time = 0.8772
        self.first_iter_time = 3.2041

class Inception4Model256(Model):
    def __init__(self):
        super(Inception4Model256, self).__init__('Inception4Model256',
                153740040 // 256,
                # [5.5325, 2.8125, 1.8716, 1.4081,
                #  1.1203, 0.9443, 0.8087, 0.7084,
                #  0.6496, 0.5976, 0.5636, 0.5279,
                #  0.4832, 0.4654, 0.4498, 0.4084,
                #  0.4086, 0.3908, 0.3766, 0.3581,
                #  0.3649, 0.3393, 0.3393, 0.3179,
                #  0.3179, 0.3046, 0.3027, 0.3027,
                #  0.2822, 0.2704, 0.2587, 0.2469,
                #  0.2478, 0.2487, 0.2496, 0.2506,
                #  0.2467, 0.2429, 0.2390, 0.2352])
                [5.5325, 2.7994, 1.8739, 1.4089,
                 1.1293, 0.9426, 0.8089, 0.7085,
                 0.6428, 0.5883, 0.5424, 0.5032,
                 0.4709, 0.4427, 0.4177, 0.3954,
                 0.3757, 0.3581, 0.3421, 0.3275,
                 0.3175, 0.3082, 0.2995, 0.2913,
                 0.2837, 0.2766, 0.2699, 0.2636,
                 0.2591, 0.2549, 0.2509, 0.2471,
                 0.2451, 0.2434, 0.2418, 0.2403,
                 0.2389, 0.2376, 0.2364, 0.2353])
        self.import_graph_time = 2.8707
        self.first_iter_time = 7.4958

class Resnet50Model128(Model):
    def __init__(self):
        super(Resnet50Model128, self).__init__('Resnet50Model128',
                153740040 // 128,
                # [0.8918, 0.4571, 0.3245, 0.2504,
                #  0.2216, 0.1983, 0.1816, 0.1613,
                #  0.1586, 0.1413, 0.1364, 0.1307,
                #  0.1268, 0.1253, 0.1207, 0.1142,
                #  0.1134, 0.1116, 0.1071, 0.1068])
                [0.89180, 0.48103, 0.32935, 0.25040,
                 0.22001, 0.19620, 0.17705, 0.16131,
                 0.15238, 0.14439, 0.13720, 0.13070,
                 0.12614, 0.12189, 0.11792, 0.11421,
                 0.11225, 0.11037, 0.10856, 0.10681])
        self.import_graph_time = 1.2863
        self.first_iter_time = 3.7210

class Resnet50Model256(Model):
    def __init__(self):
        super(Resnet50Model256, self).__init__('Resnet50Model256',
                153740040 // 256,
                [1.7870, 0.9100, 0.6052, 0.4604,
                 0.3898, 0.3368, 0.2958, 0.2625,
                 0.2437, 0.2235, 0.2124, 0.1986,
                 0.1890, 0.1832, 0.1756, 0.1631,
                 0.1628, 0.1537, 0.1495, 0.1426,
                 0.1420, 0.1355, 0.1369, 0.1306])
        self.import_graph_time = 1.2863
        self.first_iter_time = 3.7210

class Resnet50Model512(Model):
    def __init__(self):
        super(Resnet50Model512, self).__init__('Resnet50Model512',
                153740040 // 512,
                [3.5820, 1.8252, 1.2256, 0.9199,
                 0.7442, 0.6213, 0.5427, 0.4731,
                 0.4299, 0.3901, 0.3622, 0.3401,
                 0.3176, 0.2982, 0.2828, 0.2639,
                 0.2582, 0.2459, 0.2338, 0.2242,
                 0.2168, 0.2097, 0.2054, 0.1983,
                 0.1997, 0.1946, 0.1881, 0.1823,
                 0.1823, 0.1744, 0.1762, 0.1691,
                 0.1630, 0.1635, 0.1635, 0.1583,
                 0.1583, 0.1511, 0.1511, 0.1511,
                 0.1436, 0.1436, 0.1436, 0.1364,
                 0.1360, 0.1352, 0.1352, 0.1324])
        self.import_graph_time = 1.2863
        self.first_iter_time = 3.7210

class DcganModel256(Model):
    def __init__(self):
        super(DcganModel256, self).__init__('DcganModel256',
                15000000 // 256,
                # [0.3350,  0.2585,  0.1819,  0.1053,
                #  0.09790, 0.09049, 0.08308, 0.07566,
                #  0.07273, 0.06979, 0.06685, 0.06391,
                #  0.06229, 0.06066, 0.05904, 0.05741,
                #  0.05643, 0.05544, 0.05445, 0.05346,
                #  0.05315, 0.05283, 0.05252, 0.05220,
                #  0.05220, 0.05220, 0.05220, 0.05220,
                #  0.05178, 0.05134, 0.05090, 0.05046])
                [0.33500, 0.19395, 0.13649, 0.10530,
                 0.09590, 0.08805, 0.08139, 0.07567,
                 0.07233, 0.06929, 0.06650, 0.06393,
                 0.06215, 0.06048, 0.05890, 0.05741,
                 0.05637, 0.05537, 0.05441, 0.05349,
                 0.05314, 0.05282, 0.05251, 0.05223,
                 0.05196, 0.05171, 0.05148, 0.05126,
                 0.05105, 0.05085, 0.05066, 0.05048])
        self.import_graph_time = 0.5550
        self.first_iter_time = 2.6274

class ChatbotModel256(Model):
    def __init__(self):
        super(ChatbotModel256, self).__init__('ChatbotModel256',
                660000000 // 256,
                # [0.1047,  0.09067, 0.07661, 0.06255])
                [0.1047, 0.0855, 0.07226, 0.06258])
        self.import_graph_time = 0.1
        self.first_iter_time = 0.1

class VideopredictionModel64(Model):
    def __init__(self):
        super(VideopredictionModel64, self).__init__('VideopredictionModel64',
                3200000 // 64,
                # [1.1244, 0.8743, 0.6242, 0.3740,
                #  0.3534, 0.3327, 0.3121, 0.2914,
                #  0.2809, 0.2704, 0.2598, 0.2493,
                #  0.2464, 0.2436, 0.2407, 0.2378,
                #  0.2332, 0.2285, 0.2238, 0.2191,
                #  0.2162, 0.2133, 0.2103, 0.2074])
                [1.12440, 0.67373, 0.48098, 0.37400,
                 0.34923, 0.32754, 0.30840, 0.29140,
                 0.27958, 0.26869, 0.25862, 0.24930,
                 0.24497, 0.24079, 0.23676, 0.23287,
                 0.22926, 0.22577, 0.22239, 0.21911,
                 0.21600, 0.21310, 0.21030, 0.20760])
        self.import_graph_time = 6.4831
        self.first_iter_time = 17.807