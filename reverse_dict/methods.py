from collections import OrderedDict
import functools
import time


class Method (object):
    def __init__(self, non_unique_values=False, **kwargs):
        from reverse_dict.arguments import NumberTimesArgument,\
            NumberItemsArgument, PrecisionArgument, SmallTestArgument
        # TODO: add it as an option, -unu, --use_non_uniques
        # self.use_non_uniques = kwargs[UseNonUniquesArgument.__argument_name__]
        self.non_unique_values = non_unique_values
        self.kwargs = kwargs
        # Common options
        # TODO: call arguments.get_options_from_common_args()
        self.number_times = kwargs[NumberTimesArgument.__argument_name__]
        self.number_items = kwargs[NumberItemsArgument.__argument_name__]
        self.small_test = kwargs[SmallTestArgument.__argument_name__]
        self.small_test = True
        self.precision = kwargs[PrecisionArgument.__argument_name__]
        # TODO; print dicts at the end
        # self.print_dicts = kwargs[PrintDictsArgument.__argument_name__]
        # TODO: complete it!
        self.use_ordered_dict = False
        # self.use_ordered_dict = kwargs[UseOrderedDictArgument.__argument_name__]
        self.run_times = 0
        self.orig_dict = None
        self.inv_dict = None
        self.init_orig_dict()
        self.init_inv_dict()

    def init_orig_dict(self):
        #import ipdb
        #ipdb.set_trace()
        try:
            range_ = xrange
        except NameError as e:
            range_ = range
        if self.non_unique_values:
            # First half
            k1 = ['k{}'.format(i) for i in range_(1, int(self.number_items / 2) + 1)]
            v1 = ['v{}'.format(i) for i in range_(1, int(self.number_items / 2) + 1)]
            dict1 = dict(zip(k1, v1))
            # Second half: different keys but same values as in first half
            k2 = ['k{}'.format(i) for i in range_(int(self.number_items / 2) + 1, self.number_items + 1)]
            v2 = ['v{}'.format(i) for i in range_(1, int(self.number_items / 2) + 2)]
            dict2 = dict(zip(k2, v2))
            # Merge both halves
            dict1.update(dict2)
            self.orig_dict = dict1
        else:
            k = ['k{}'.format(i) for i in range_(1, self.number_items + 1)]
            v = ['v{}'.format(i) for i in range_(1, self.number_items + 1)]
            self.orig_dict = dict(zip(k, v))
        #ipdb.set_trace()

    def init_inv_dict(self):
        if self.use_ordered_dict:
            self.inv_dict = OrderedDict({})
        else:
            self.inv_dict = {}

    @staticmethod
    def reset_data(func):
        @functools.wraps(func)
        def wrapper_reset_data(self, *args, **kwargs):
            # TODO: to be used and tested
            self.run_times = 0
            self.init_orig_dict()
            self.init_inv_dict()
            func(self, *args, **kwargs)
        return wrapper_reset_data

    def compute_avg_run_time(self):
        raise NotImplementedError()

    def get_unused_kwargs(self):
        all_keys = set(self.__dict__.keys())
        keys_from_kwargs = set(self.kwargs.keys())
        unused_keys = keys_from_kwargs - all_keys
        return list(unused_keys)

    def print_run_time(self, n, duration):
        print('#{} Run time: {:.{}f}'.format(n, duration, self.precision))

    def print_avg_run_time(self):
        print('Avg run time: {:.{}f} seconds'.format(
            (self.run_times / self.number_times),
            self.precision))

    @staticmethod
    def timer(func):
        @functools.wraps(func)
        def wrapper_timer(self, *args, **kwargs):
            wrapper_timer.num_calls += 1
            start_time = time.perf_counter()
            retval = func(self, *args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            self.run_times += run_time
            self.print_run_time(wrapper_timer.num_calls, run_time)
            return retval
        wrapper_timer.num_calls = 0
        return wrapper_timer

    def reverse_dict(self, dict_):
        raise NotImplementedError()


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
        for i in xrange(1, self.number_times + 1):
            start_time = time.time()
            if self.use_items:
                self.inv_dict = {v: k for k, v in self.orig_dict.items()}
            else:
                self.inv_dict = {v: k for k, v in self.orig_dict.iteritems()}
            duration = time.time() - start_time
            self.run_times += duration
            self.print_run_time(i, duration)

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
        for i in range(1, self.number_times + 1):
            start_time = time.time()
            self.inv_dict = {v: k for k, v in self.orig_dict.items()}
            duration = time.time() - start_time
            self.run_times += duration
            self.print_run_time(i, duration)

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
        super(Method02Py2, self).__init__(non_unique_values=True, **kwargs)
        # Extra options that are specific to this method
        self.use_items = self.kwargs[UseItemsArgument.__argument_name__]

    def compute_avg_run_time(self):
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
            self.run_times += duration
            self.print_run_time(i, duration)

        self.print_avg_run_time()
        if self.small_test:
            print(self.orig_dict)
            print(self.inv_dict)


class Method02Py3(Method):
    __method_name__ = 'method_02_py3'
    __python_version__ = 'python3'

    def __init__(self, **kwargs):
        super().__init__(non_unique_values=True, **kwargs)

    def compute_avg_run_time(self):
        for i in range(1, self.number_times + 1):
            start_time = time.time()
            self.inv_dict = {}
            for k, v in self.orig_dict.items():
                self.inv_dict[v] = self.inv_dict.get(v, [])
                self.inv_dict[v].append(k)
            duration = time.time() - start_time
            self.run_times += duration
            self.print_run_time(i, duration)

        self.print_avg_run_time()
        if self.small_test:
            print(self.orig_dict)
            print(self.inv_dict)


class Method03Py2(Method):
    __method_name__ = 'method_03_py2'
    __python_version__ = 'python2'

    def __init__(self, **kwargs):
        # Lazy import
        from reverse_dict.arguments import UseItemsArgument
        super(Method03Py2, self).__init__(**kwargs)
        # Extra options that are specific to this method
        self.use_items = self.kwargs[UseItemsArgument.__argument_name__]

    def reverse_dict(self, dict_):
        if self.use_items:
            items = self.orig_dict.items()
        else:
            items = self.orig_dict.iteritems()
        return dict_.__class__(map(reversed, items))

    @Method.reset_data
    def compute_avg_run_time(self):
        for i in range(1, self.number_times + 1):
            start_time = time.time()
            self.inv_dict = self.reverse_dict(self.orig_dict)
            duration = time.time() - start_time
            self.run_times += duration
            self.print_run_time(i, duration)

        self.print_avg_run_time()
        if self.small_test:
            print(self.orig_dict)
            print(self.inv_dict)


class Method03Py3(Method):
    __method_name__ = 'method_03_py3'
    __python_version__ = 'python3'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Method.timer
    def reverse_dict(self, dict_):
        return dict_.__class__(map(reversed, dict_.items()))

    @Method.reset_data
    def compute_avg_run_time(self):
        for i in range(1, self.number_times + 1):
            self.inv_dict = self.reverse_dict(self.orig_dict)

        self.print_avg_run_time()
        if self.small_test:
            print(self.orig_dict)
            print(self.inv_dict)
