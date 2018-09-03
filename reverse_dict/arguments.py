from reverse_dict.methods import (Method01Py2, Method01Py3, Method02Py2,
                                  Method02Py3, Method03Py2, Method03Py3)
from reverse_dict.config import cfg


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
                   unique values. Works on Python 2.7
    {}: the reversed dict stores as values a list of all the keys
                   associated with the same value in the original dict,
                   and the dict doesn't contain unique values. Works on
                   Python 2.7
    {}: makes use of map(reversed,), and the type and order of the
                   original dict are preserved (if for example it is an
                   OrderedDict). Works on Python 2.7

    {}: Python 3 version of {}
    {}: Python 3 version of {}
    {}: Python 3 version of {}
    '''.format(Method01Py2.__method_name__, Method02Py2.__method_name__,
               Method03Py2.__method_name__, Method01Py3.__method_name__,
               Method01Py2.__method_name__, Method02Py3.__method_name__,
               Method02Py2.__method_name__, Method03Py3.__method_name__,
               Method03Py2.__method_name__)
    __common_option__ = True

    def __init__(self, option_name=None, short_option='-m',
                 long_option='--{}'.format(__argument_name__),
                 default=Method01Py3.__method_name__, help=help_arg, **kwargs):
        super(MethodNameArgument, self).__init__(option_name, short_option,
                                                 long_option, default=default,
                                                 help=help, **kwargs)


class NumberItemsArgument(Argument):
    __argument_name__ = 'number_items'
    __common_option__ = True

    help_arg = 'Number of items in the dictionary.'

    def __init__(self, option_name=None, short_option='-ni',
                 long_option='--{}'.format(__argument_name__), default=10000,
                 type=int, help=help_arg, **kwargs):
        super(NumberItemsArgument, self).__init__(option_name, short_option,
                                                  long_option, default=default,
                                                  type=type, help=help, **kwargs)


class NumberTimesArgument(Argument):
    __argument_name__ = 'number_times'
    help_arg = '''Number of times the dictionary's keys and values will be reversed. 
Each time, the run time of the reversal is computed and at the end 
of all the tries, the average run time is computed.
    '''
    __common_option__ = True

    def __init__(self, option_name=None, short_option='-nt',
                 long_option='--{}'.format(__argument_name__), default=10, type=int,
                 help=help_arg, **kwargs):
        super(NumberTimesArgument, self).__init__(option_name, short_option,
                                                  long_option, default=default,
                                                  type=type, help=help, **kwargs)


class PrecisionArgument(Argument):
    __argument_name__ = 'precision'
    __common_option__ = True

    help_arg = 'Decimal precision used when displaying number results.'

    def __init__(self, option_name=None, short_option='-p', type=int,
                 long_option='--{}'.format(__argument_name__), default=4,
                 help=help_arg, **kwargs):
        super(PrecisionArgument, self).__init__(option_name, short_option,
                                                long_option, default=default,
                                                type=type, help=help, **kwargs)


class PrintDictsArgument(Argument):
    __argument_name__ = 'print_dicts'
    __common_option__ = True

    help_arg = 'Print the original and reversed dictionaries at the end.'

    def __init__(self, option_name=None, short_option='-pd',
                 long_option='--{}'.format(__argument_name__), action='store_true',
                 help=help_arg, **kwargs):
        super(PrintDictsArgument, self).__init__(option_name, short_option,
                                                 long_option, action=action,
                                                  help=help, **kwargs)


class UseItemsArgument(Argument):
    __argument_name__ = 'use_items'
    __common_option__ = False

    help_arg = '''When working on Python 2, use dict.items() instead of the more efficient 
dict.iteritems() (default).'''

    def __init__(self, option_name=None, short_option='-ui',
                 long_option='--{}'.format(__argument_name__), action='store_true',
                 help=help_arg, **kwargs):
        super(UseItemsArgument, self).__init__(option_name, short_option,
                                               long_option, action=action,
                                               help=help, **kwargs)


class UseNonUniquesArgument(Argument):
    __argument_name__ = 'use_non_uniques'
    __common_option__ = True

    help_arg = 'Initialize the original dictionary with non-unique values.'

    def __init__(self, option_name=None, short_option='-unu',
                 long_option='--{}'.format(__argument_name__), action='store_true',
                 help=help_arg, **kwargs):
        super(UseNonUniquesArgument, self).__init__(option_name, short_option,
                                                    long_option, action=action,
                                                    help=help, **kwargs)


class UseOrderedDictArgument(Argument):
    __argument_name__ = 'use_ordered_dict'
    __common_option__ = True

    help_arg = 'Use OrderedDict instead of dict (default).'

    def __init__(self, option_name=None, short_option='-uod',
                 long_option='--{}'.format(__argument_name__), action='store_true',
                 help=help_arg, **kwargs):
        super(UseOrderedDictArgument, self).__init__(option_name, short_option,
                                                     long_option, action=action,
                                                     help=help, **kwargs)


class UseSetDefaultArgument(Argument):
    __argument_name__ = 'use_setdefault'
    __common_option__ = False

    help_arg = 'Use dict.setdefault() instead of dict.get() (default) when populating the dictionary.'

    def __init__(self, option_name=None, short_option='-usd',
                 long_option='--{}'.format(__argument_name__), action='store_true',
                 help=help_arg, **kwargs):
        super(UseSetDefaultArgument, self).__init__(option_name, short_option,
                                                    long_option, action=action,
                                                    help=help, **kwargs)


class VersionArgument(Argument):
    __argument_name__ = 'version'
    __common_option__ = True

    help_arg = "Show program's version and exit."

    def __init__(self, option_name=None, short_option='-v',
                 long_option='--{}'.format(__argument_name__),  action='version',
                 version='%(prog)s {}'.format(cfg.version), help=help_arg,
                 **kwargs):
        super(VersionArgument, self).__init__(option_name, short_option,
                                              long_option, action=action,
                                              version=version, help=help,
                                              **kwargs)


# TODO: add also a get_all_arguments() function to be used in the main script
def get_common_arguments():
    # TODO: make use of `__common_option__` to know which argument to add to the list
    return [NumberItemsArgument(), NumberTimesArgument(), PrecisionArgument(),
            PrintDictsArgument(), UseNonUniquesArgument(), UseOrderedDictArgument(),
            VersionArgument()]
