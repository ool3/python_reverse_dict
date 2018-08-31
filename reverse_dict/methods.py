from collections import OrderedDict
import time


class Method (object):
    def __init__(self, unique_values=True, **kwargs):
        from reverse_dict.arguments import NumberTimesArgument,\
            NumberItemsArgument, PrecisionArgument, SmallTestArgument
        self.unique_values = unique_values
        self.kwargs = kwargs
        # Common options
        # TODO: call arguments.get_options_from_common_args()
        self.number_times = kwargs[NumberTimesArgument.__argument_name__]
        self.number_items = kwargs[NumberItemsArgument.__argument_name__]
        self.small_test = kwargs[SmallTestArgument.__argument_name__]
        self.precision = kwargs[PrecisionArgument.__argument_name__]
        # TODO: complete it
        self.use_ordered_dict = False
        # self.use_ordered_dict = kwargs[PrecisionArgument.__argument_name__]
        self.durations = 0
        self.orig_dict = self._init_orig_dict()
        self.inv_dict = None

    def _init_orig_dict(self):
        if self.small_test:
            self.number_times = 1
            self.number_items = 1
            if self.unique_values:
                return {1: 'a', 2: 'b', 3: 'c', 4: 'a', 5: 'b', 6: 'b'}
            else:
                return {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
        else:
            if self.unique_values:
                # my_dict = dict(zip(range(1, int(n_items / 2) + 1), range(1, int(n_items / 2) + 1)))
                # my_dict.update(dict(zip(range(int(n_items / 2) + 1, n_items + 1), range(1, int(n_items / 2) + 1))))
                return {}
            else:
                return dict(zip(range(1, self.number_items + 1), range(-self.number_items, 0)))

    def _init_inv_dict(self):
        if self.use_ordered_dict:
            return OrderedDict({})
        else:
            return {}

    def reset_data(self):
        # TODO: to be used and tested
        self.durations = 0
        self.inv_dict = None

    def compute_avg_run_time(self):
        raise NotImplementedError()

    def get_unused_kwargs(self):
        all_keys = set(self.__dict__.keys())
        keys_from_kwargs = set(self.kwargs.keys())
        unused_keys = keys_from_kwargs - all_keys
        return list(unused_keys)

    def print_duration(self, count, duration):
        print('#{} Duration: {:.{}f}'.format(count, duration, self.precision))

    def print_avg_run_time(self):
        print('Avg: {:.{}f} seconds'.format((self.durations / self.number_times),
                                            self.precision))


class Method01Py2(Method):
    __method_name__ = 'method_01_py2'
    __python_version__ = 'python2'

    def __init__(self, **kwargs):
        # Lazy import
        from reverse_dict.arguments import UseItemsArgument
        super(Method01Py2, self).__init__(**kwargs)
        # Extra options that are specific to this method
        self.use_items = self.kwargs[UseItemsArgument.__argument_name__]

    def compute_avg_run_time(self):
        # TODO: drop count
        count = 1
        for i in xrange(self.number_times):
            start_time = time.time()
            if self.use_items:
                self.inv_dict = {v: k for k, v in self.orig_dict.items()}
            else:
                self.inv_dict = {v: k for k, v in self.orig_dict.iteritems()}
            duration = time.time() - start_time
            self.durations += duration
            self.print_duration(count, duration)
            count += 1

        self.print_avg_run_time()
        if self.small_test:
            print(self.orig_dict)
            print(self.inv_dict)


class Method01Py3(Method):
    __method_name__ = 'method_01_py3'
    __python_version__ = 'python3'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def compute_avg_run_time(self):
        # TODO: drop count
        count = 1
        for i in range(self.number_times):
            start_time = time.time()
            self.inv_dict = {v: k for k, v in self.orig_dict.items()}
            duration = time.time() - start_time
            self.durations += duration
            self.print_duration(count, duration)
            count += 1

        self.print_avg_run_time()
        if self.small_test:
            print(self.orig_dict)
            print(self.inv_dict)


class Method02Py2(Method):
    __method_name__ = 'method_02_py2'
    __python_version__ = 'python2'

    def __init__(self, **kwargs):
        # Lazy import
        from reverse_dict.arguments import UseItemsArgument
        super(Method02Py2, self).__init__(unique_values=True, **kwargs)
        # Extra options that are specific to this method
        self.use_items = self.kwargs[UseItemsArgument.__argument_name__]

    def compute_avg_run_time(self):
        self.reset_data()
        for i in range(1, self.number_times + 1):
            start_time = time.time()
            self.inv_dict = {}
            if self.use_items:
                items = self.orig_dict.items()
            else:
                items = self.orig_dict.iteritems()
            for k, v in items:
                self.inv_dict[v] = self.inv_dict.get(v, [])
                self.inv_dict[v].append(k)
            duration = time.time() - start_time
            self.durations += duration
            self.print_duration(i, duration)

        self.print_avg_run_time()
        if self.small_test:
            print(self.orig_dict)
            print(self.inv_dict)
