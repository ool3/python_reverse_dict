import time


class Method (object):
    def __init__(self, **kwargs):
        from reverse_dict.arguments import NumberTimesArgument,\
            NumberItemsArgument, PrecisionArgument, SmallTestArgument
        self.kwargs = kwargs
        # Common options
        self.number_times = kwargs[NumberTimesArgument.__argument_name__]
        self.number_items = kwargs[NumberItemsArgument.__argument_name__]
        self.small_test = kwargs[SmallTestArgument.__argument_name__]
        self.precision = kwargs[PrecisionArgument.__argument_name__]
        self.durations = 0
        self.my_dict = self._init_data()
        self.inv_dict = None

    def compute_avg_run_time(self):
        pass

    def _init_data(self):
        if self.small_test:
            self.number_times = 1
            self.number_items = 1
            return {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
        else:
            return dict(zip(range(1, self.number_items + 1),
                            range(-self.number_items, 0)))

    def print_duration(self, count, duration):
        print('#{} Duration: {:.{}f}'.format(count, duration, self.precision))

    def print_avg_run_time(self):
        print('Avg: {:.{}f} seconds'.format((self.durations / self.number_items),
                                            self.precision))


class Method01Py2(Method):
    __method_name__ = 'method_01_py2'

    def __init__(self, **kwargs):
        from reverse_dict.arguments import UseItemsArgument
        super(Method01Py2, self).__init__(**kwargs)
        # Extra options that are specific to this method
        self.use_items = self.kwargs[UseItemsArgument.__argument_name__]

    def compute_avg_run_time(self):
        count = 1
        for i in xrange(self.number_times):
            start_time = time.time()
            if self.use_items:
                self.inv_dict = {v: k for k, v in self.my_dict.items()}
            else:
                self.inv_dict = {v: k for k, v in self.my_dict.iteritems()}
            duration = time.time() - start_time
            self.durations += duration
            self.print_duration(count, duration)
            count += 1

        self.print_avg_run_time()
        if self.small_test:
            print(self.my_dict)
            print(self.inv_dict)


class Method01Py3(Method):
    __method_name__ = 'method_01_py3'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def compute_avg_run_time(self):
        count = 1
        for i in range(self.number_times):
            start_time = time.time()
            self.inv_dict = {v: k for k, v in self.my_dict.items()}
            duration = time.time() - start_time
            self.durations += duration
            self.print_duration(count, duration)
            count += 1

        self.print_avg_run_time()
        if self.small_test:
            print(self.my_dict)
            print(self.inv_dict)
