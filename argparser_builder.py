import argparse
import textwrap
import ipdb

from argument_names import argument_names as an
from method_names import method_names as mn


class ArgParserBuilder:
    def __init__(self, method_name, script_description='', list_arguments=[]):
        self.method_name = method_name
        self.script_description = script_description
        self.list_arguments = list_arguments
        self.parser = self._get_arg_parser()

    def get_parser(self):
        return self.parser

    def _get_arg_parser(self):
        parser = argparse.ArgumentParser(
            # prog='compute_running_times',
            description=textwrap.dedent(self.script_description),
            formatter_class=argparse.RawTextHelpFormatter)
        self._add_arguments(parser)
        return parser

    def _add_arguments(self, parser):
        for arg in self.list_arguments:
            parser.add_argument(*arg.args, **arg.kwargs)


class Argument:
    def __init__(self, option_name, short_option, long_option, **kwargs):
        self.args = None
        self.kwargs = {}
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
    __argument_name__ = an.method_name
    help_arg = '''\
    Name of the method that reverses a dict's keys and values:

    method_01_py2: makes use of dict comprehension, and the dict must contain
                   unique values
    method_02_py2: makes use of dict.get(), and the dict doesn't contain
                   unique values
    method_03_py2: makes use of map(reversed,), and the type and order of the
                   original dict are preserved (if for example it is an
                   OrderedDict)

    method_01_py3: Python 3 version of method-01-py2
    method_02_py3: Python 3 version of method-02-py3
    method_03_py3: Python 3 version of method-03-py2
    '''

    def __init__(self, option_name=None, short_option='-m',
                 long_option='--method_name', default=mn.method_01_py3,
                 help=help_arg, **kwargs):
        super().__init__(option_name, short_option, long_option, default=default,
                         help=help, **kwargs)


class NumberTimesArgument(Argument):
    __argument_name__ = an.number_times
    help_arg = '''\
    Number of times the dictionary's keys and values will be reversed.
    '''

    def __init__(self, option_name=None, short_option='-n',
                 long_option='--number_times', default=10, type=int,
                 help=help_arg, **kwargs):
        super().__init__(option_name, short_option, long_option, default=default,
                         type=type, help=help, **kwargs)


class NumberItemsArgument(Argument):
    __argument_name__ = an.number_items

    help_arg = '''\
    Number of items in the dictionary.
    '''

    def __init__(self, option_name=None, short_option='-i',
                 long_option='--number_items', default=10000, type=int,
                 help=help_arg, **kwargs):
        super().__init__(option_name, short_option, long_option, default=default,
                         type=type, help=help, **kwargs)


class PrecisionArgument(Argument):
    __argument_name__ = an.precision

    help_arg = '''\
    Decimal precision used when displaying number results.
    '''

    def __init__(self, option_name=None, short_option='-p', type=int,
                 long_option='--precision', default=4, help=help_arg, **kwargs):
        super().__init__(option_name, short_option, long_option, default=default,
                         type=type, help=help, **kwargs)


class UseItemsArgument(Argument):
    __argument_name__ = an.use_items

    help_arg = '''\
    When working on Python 2, use dict.items() instead of the more efficient
    dict.iteritems().
    '''

    def __init__(self, option_name=None, short_option='-ui',
                 long_option='--use_items', action='store_true', help=help_arg,
                 **kwargs):
        super().__init__(option_name, short_option, long_option, action=action,
                         help=help, **kwargs)


class UseSetDefaultArgument(Argument):
    __argument_name__ = an.use_setdefault

    help_arg = '''\
    Use dict.setdefault() instead of dict.get() when populating the dictionary.
    '''

    def __init__(self, option_name=None, short_option='-usd',
                 long_option='--use_setdefault', action='store_true',
                 help=help_arg, **kwargs):
        super().__init__(option_name, short_option, long_option, action=action,
                         help=help, **kwargs)


class SmallTestArgument(Argument):
    __argument_name__ = an.small_test

    help_arg = '''\
    Use a small dictionary with few items which the keys and values will be
    reversed.
    '''

    def __init__(self, option_name=None, short_option='-s',
                 long_option='--small_test', action='store_true', help=help_arg,
                 **kwargs):
        super().__init__(option_name, short_option, long_option, action=action,
                         help=help, **kwargs)


def get_common_arguments():
    return [MethodNameArgument(), NumberItemsArgument(), NumberTimesArgument(),
            PrecisionArgument(), SmallTestArgument()]
