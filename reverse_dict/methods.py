from collections import OrderedDict
import functools
import time


# Abstract class for all methods (Python 2 & 3)
class Method (object):
    def __init__(self, **kwargs):
        # TODO: make use of Argument.`__common_option__` to know what arguments
        # have options that are common to all methods
        from reverse_dict.arguments import NumberTimesArgument,\
            NumberItemsArgument, PrecisionArgument, PrintDictsArgument,\
            UseNonUniquesArgument, UseOrderedDictArgument
        self.kwargs = kwargs
        # Common options
        self.number_times = kwargs[NumberTimesArgument.__argument_name__]
        self.number_items = kwargs[NumberItemsArgument.__argument_name__]
        self.precision = kwargs[PrecisionArgument.__argument_name__]
        self.use_non_uniques = kwargs[UseNonUniquesArgument.__argument_name__]
        self.print_dicts = kwargs[PrintDictsArgument.__argument_name__]
        self.use_ordered_dict = kwargs[UseOrderedDictArgument.__argument_name__]
        try:
            # Python 2 uses xrange
            self.range_ = xrange
        except NameError as e:
            # Python 3 uses range (same as xrange in Python 2)
            self.range_ = range
        self.run_times = 0
        self.orig_dict = None
        self.inv_dict = self.get_empty_dict()
        self._init_orig_dict()

    def _init_orig_dict(self):
        if self.use_non_uniques:
            # First half
            k1 = ['k{}'.format(i) for i in self.range_(1, int(self.number_items / 2) + 1)]
            v1 = ['v{}'.format(i) for i in self.range_(1, int(self.number_items / 2) + 1)]
            dict1 = self.init_dict(zip(k1, v1))
            # Second half: different keys but same values as in first half
            k2 = ['k{}'.format(i) for i in self.range_(int(self.number_items / 2) + 1, self.number_items + 1)]
            v2 = ['v{}'.format(i) for i in self.range_(1, int(self.number_items / 2) + 2)]
            dict2 = self.init_dict(zip(k2, v2))
            # Merge both halves
            dict1.update(dict2)
            self.orig_dict = dict1
        else:
            k = ['k{}'.format(i) for i in self.range_(1, self.number_items + 1)]
            v = ['v{}'.format(i) for i in self.range_(1, self.number_items + 1)]
            self.orig_dict = self.init_dict(zip(k, v))

    def init_dict(self, list_tuple):
        dict_type = OrderedDict if self.use_ordered_dict else dict
        return dict_type(list_tuple)

    def get_empty_dict(self):
        return OrderedDict() if self.use_ordered_dict else {}

    @staticmethod
    def get_items(dict_):
        return dict_.items()

    def get_unused_kwargs(self):
        all_keys = set(self.__dict__.keys())
        keys_from_kwargs = set(self.kwargs.keys())
        unused_keys = keys_from_kwargs - all_keys
        return list(unused_keys)

    def print_avg_run_time(self):
        print('Avg run time: {:.{}f} seconds'.format(
            (self.run_times / self.number_times),
            self.precision))
        if self.print_dicts:
            print('\nOriginal dict:\n{}'.format(self.orig_dict))
            print('Inverse dictionary:\n{}'.format(self.inv_dict))

    def print_run_time(self, i, duration):
        print('#{} Run time: {:.{}f}'.format(i, duration, self.precision))

    def reset_data(func):
        @functools.wraps(func)
        def wrapper_reset_data(self, *args, **kwargs):
            self.run_times = 0
            func(self, *args, **kwargs)
        return wrapper_reset_data

    @reset_data
    def compute_avg_run_time(self):
        for _ in self.range_(1, self.number_times + 1):
            self.inv_dict = self.reverse_orig_dict()
        self.print_avg_run_time()

    def reverse_orig_dict(self):
        raise NotImplementedError()

    @staticmethod
    def timer(func):
        @functools.wraps(func)
        def wrapper_timer(self, *args, **kwargs):
            wrapper_timer.num_calls += 1
            start_time = time.perf_counter()
            # start_time = time.time()
            retval = func(self, *args, **kwargs)
            end_time = time.perf_counter()
            # end_time = time.time()
            run_time = end_time - start_time
            self.run_times += run_time
            self.print_run_time(wrapper_timer.num_calls, run_time)
            return retval
        wrapper_timer.num_calls = 0
        return wrapper_timer


# Abstract class only for Python2-based Methods
class MethodPy2(Method):
    def __init__(self, **kwargs):
        super(MethodPy2, self).__init__(**kwargs)
        # Lazy import
        from reverse_dict.arguments import UseItemsArgument
        # Extra options that are specific to Python2-based methods
        self.use_items = self.kwargs[UseItemsArgument.__argument_name__]
        self.orig_dict_items = self.get_items(self.orig_dict)

    # Override parent's method
    def get_items(self, dict_):
        # dict.iteritems() returns an iterator, not a list of values like
        # dict.items() does
        return dict_.items() if self.use_items else \
            [(k, v) for k, v in dict_.iteritems()]

    # Override parent's method
    def reverse_orig_dict(self):
        raise NotImplementedError()

    # Override parent's method
    # No perf_counter() in Python2
    @staticmethod
    def timer(func):
        @functools.wraps(func)
        def wrapper_timer(self, *args, **kwargs):
            wrapper_timer.num_calls += 1
            start_time = time.time()
            retval = func(self, *args, **kwargs)
            end_time = time.time()
            run_time = end_time - start_time
            self.run_times += run_time
            self.print_run_time(wrapper_timer.num_calls, run_time)
            return retval
        wrapper_timer.num_calls = 0
        return wrapper_timer


class Method01Py2(MethodPy2):
    __method_name__ = 'method_01_py2'
    __python_version__ = 'python2'
    __method_description__ = '''
    %(prog)s works with Python 2 by reversing a dict's keys and values using a 
    dict comprehension, and assumes that the dict contains UNIQUE values. Also, by 
    default dict.iteritems() is used when populating the reversed dict. Use the option 
    -ui, --use_items to instead use dict.items() which is less efficient.
    '''

    def __init__(self, **kwargs):
        super(Method01Py2, self).__init__(**kwargs)

    @MethodPy2.timer
    def reverse_orig_dict(self):
        # Dict comprehension template for Python 2.7+:
        # {key:value for (key,value) in dictionary.items()}
        # Dict comprehension template in Python2.6:
        # dict((key, value) for (key, value) in dictionary.items())
        # ref.: https://bit.ly/2Ce9xjm and https://stackoverflow.com/a/14507623
        if self.use_items:
            items = self.orig_dict.items()
        else:
            items = self.orig_dict.iteritems()
        if self.use_ordered_dict:
            return OrderedDict((v, k) for k, v in items)
        else:
            return {v: k for k, v in items}


class Method01Py3(Method):
    __method_name__ = 'method_01_py3'
    __python_version__ = 'python3'
    __method_description__ = '''
    %(prog)s works with Python 3 by reversing a dict's keys and values using a dict 
    comprehension, and assumes that the dict contains UNIQUE values.
    '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orig_dict_items = self.get_items(self.orig_dict)

    @Method.timer
    def reverse_orig_dict(self):
        # TODO: Factorize. Method01Py2 and Method01Py3 have the same method.
        import ipdb
        ipdb.set_trace()
        if self.use_ordered_dict:
            return OrderedDict((v, k) for k, v in self.orig_dict_items)
        else:
            return {v: k for k, v in self.orig_dict_items}
            # Initial insertion order not respected:
            # return {(v, k) for k, v in self.orig_dict_items}


class Method02Py2(MethodPy2):
    __method_name__ = 'method_02_py2'
    __python_version__ = 'python2'
    __method_description__ = '''
    %(prog)s works with Python 2 by reversing a dict's keys and values. 
    It saves all the keys associated with the same values in a list. It makes 
    use of dict.get() by default when populating the reversed dict, and assumes 
    that the dict contains NON-UNIQUE values.
    '''

    def __init__(self, **kwargs):
        super(Method02Py2, self).__init__(**kwargs)

    @MethodPy2.timer
    def reverse_orig_dict(self):
        # TODO: Factorize. Method02Py2 and Method02Py3 have the same method.
        # Init inverse dict
        inv_dict = self.get_empty_dict()
        for k, v in self.orig_dict_items:
            inv_dict[v] = inv_dict.get(v, [])
            inv_dict[v].append(k)
        return inv_dict


class Method02Py3(Method):
    __method_name__ = 'method_02_py3'
    __python_version__ = 'python3'
    __method_description__ = '''
    %(prog)s works with Python 3 by reversing a dict's keys and values. 
    It saves all the keys associated with the same values in a list. It makes 
    use of dict.get() by default when populating the reversed dict, and assumes 
    that the dict contains NON-UNIQUE values.
    '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orig_dict_items = self.get_items(self.orig_dict)

    @Method.timer
    def reverse_orig_dict(self):
        # Init inverse dict
        inv_dict = self.get_empty_dict()
        for k, v in self.orig_dict_items:
            inv_dict[v] = inv_dict.get(v, [])
            inv_dict[v].append(k)
        return inv_dict


class Method03Py2(MethodPy2):
    __method_name__ = 'method_03_py2'
    __python_version__ = 'python2'
    __method_description__ = '''
    %(prog)s works with Python 2 by reversing a dict's keys and values. 
    It makes use of map(reversed,), useful when the type and order of the original 
    dictionary must be preserved (e.g. OrderedDict).
    '''

    def __init__(self, **kwargs):
        super(Method03Py2, self).__init__(**kwargs)

    @MethodPy2.timer
    def reverse_orig_dict(self):
        # TODO: Factorize. Method03Py2 and Method03Py3 have the same method
        # NOTE: try self.orig_dict.__class__
        if self.use_ordered_dict:
            return OrderedDict(map(reversed, self.orig_dict_items))
        else:
            # return dict(map(reversed, self.orig_dict_items))
            return dict(map(reversed, self.orig_dict_items))


class Method03Py3(Method):
    __method_name__ = 'method_03_py3'
    __python_version__ = 'python3'
    __method_description__ = '''
    %(prog)s works with Python 3 by reversing a dict's keys and values. 
    It makes use of map(reversed,), useful when the type and order of the original 
    dictionary must be preserved (e.g. OrderedDict).
    '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orig_dict_items = self.get_items(self.orig_dict)

    @Method.timer
    def reverse_orig_dict(self):
        # NOTE: try self.orig_dict.__class__
        if self.use_ordered_dict:
            return OrderedDict(map(reversed, self.orig_dict_items))
        else:
            # return dict(map(reversed, self.orig_dict_items))
            return dict(map(reversed, self.orig_dict_items))
