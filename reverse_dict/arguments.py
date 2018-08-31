from reverse_dict.methods import Method01Py2, Method01Py3


class Argument(object):
    def __init__(self, option_name, short_option, long_option, **kwargs):
        self.args = None
        self.kwargs = {}
        self.option_name = option_name
        self.short_option = short_option
        self.long_option = long_option
        if option_name:
            self.args = option_name
        else:
            self.args = []
            if short_option:
                self.args.append(short_option)
            if long_option:
                self.args.append(long_option)
        if kwargs:
            self.kwargs.update(kwargs)


class MethodNameArgument(Argument):
    __argument_name__ = 'method_name'
    help_arg = '''\
    Name of the method that reverses a dict's keys and values:

    {}: makes use of dict comprehension, and the dict must contain
                   unique values
    {}: makes use of dict.get(), and the dict doesn't contain
                   unique values
    {}: makes use of map(reversed,), and the type and order of the
                   original dict are preserved (if for example it is an
                   OrderedDict)

    {}: Python 3 version of method-01-py2
    {}: Python 3 version of method-02-py3
    {}: Python 3 version of method-03-py2
    '''.format(Method01Py2.__method_name__, Method01Py2.__method_name__,
               Method01Py2.__method_name__, Method01Py3.__method_name__,
               Method01Py3.__method_name__, Method01Py3.__method_name__)

    def __init__(self, option_name=None, short_option='-m',
                 long_option='--method_name', default=Method01Py3.__method_name__,
                 help=help_arg, **kwargs):
        super(MethodNameArgument, self).__init__(option_name, short_option,
                                                 long_option, default=default,
                                                 help=help, **kwargs)


class NumberItemsArgument(Argument):
    __argument_name__ = 'number_items'

    help_arg = '''\
    Number of items in the dictionary.
    '''

    def __init__(self, option_name=None, short_option='-i',
                 long_option='--number_items', default=10000, type=int,
                 help=help_arg, **kwargs):
        super(NumberItemsArgument, self).__init__(option_name, short_option,
                                                  long_option, default=default,
                                                  type=type, help=help, **kwargs)


class NumberTimesArgument(Argument):
    __argument_name__ = 'number_times'
    help_arg = '''\
    Number of times the dictionary's keys and values will be reversed.
    '''

    def __init__(self, option_name=None, short_option='-n',
                 long_option='--number_times', default=10, type=int,
                 help=help_arg, **kwargs):
        super(NumberTimesArgument, self).__init__(option_name, short_option,
                                                  long_option, default=default,
                                                  type=type, help=help, **kwargs)


class PrecisionArgument(Argument):
    __argument_name__ = 'precision'

    help_arg = '''\
    Decimal precision used when displaying number results.
    '''

    def __init__(self, option_name=None, short_option='-p', type=int,
                 long_option='--precision', default=4, help=help_arg, **kwargs):
        super(PrecisionArgument, self).__init__(option_name, short_option,
                                                long_option, default=default,
                                                type=type, help=help, **kwargs)


class SmallTestArgument(Argument):
    __argument_name__ = 'small_test'

    help_arg = '''\
    Use a small dictionary with few items which the keys and values will be
    reversed.
    '''

    def __init__(self, option_name=None, short_option='-s',
                 long_option='--small_test', action='store_true', help=help_arg,
                 **kwargs):
        super(SmallTestArgument, self).__init__(option_name, short_option,
                                                long_option, action=action,
                                                help=help, **kwargs)


class UseItemsArgument(Argument):
    __argument_name__ = 'use_items'

    help_arg = '''\
    When working on Python 2, use dict.items() instead of the more efficient
    dict.iteritems().
    '''

    def __init__(self, option_name=None, short_option='-ui',
                 long_option='--use_items', action='store_true', help=help_arg,
                 **kwargs):
        super(UseItemsArgument, self).__init__(option_name, short_option,
                                               long_option, action=action,
                                               help=help, **kwargs)


class UseSetDefaultArgument(Argument):
    __argument_name__ = 'use_setdefault'

    help_arg = '''\
    Use dict.setdefault() instead of dict.get() when populating the dictionary.
    '''

    def __init__(self, option_name=None, short_option='-usd',
                 long_option='--use_setdefault', action='store_true',
                 help=help_arg, **kwargs):
        super(UseSetDefaultArgument, self).__init__(option_name, short_option,
                                                    long_option, action=action,
                                                    help=help, **kwargs)


def get_common_arguments():
    return [SmallTestArgument(), NumberItemsArgument(), NumberTimesArgument(),
            PrecisionArgument()]
