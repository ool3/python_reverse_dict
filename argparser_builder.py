import argparse
import textwrap
import ipdb

from method import method_names as mn


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


class ArgumentNames:
    def __init__(self):
        self.method_name = 'method_name'
        self.number_times = 'number_times'
        self.number_items = 'number_items'
        self.precision = 'precision'
        self.use_items = 'use_items'
        self.use_setdefault = 'use_setdefault'
        self.small_test = 'small_test'


argument_names = ArgumentNames()


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
    __argument_name__ = argument_names.method_name
    help_arg = '''\
    Name of the method that reverses a dict:

    method_01_py2: makes use of dict comprehension, and the dict must contain
                   unique values
    method_02_py2: makes use of dict.get(), and the dict doesn't contain unique values
    method_03_py2: makes use of map(reversed,), and the type and order of the original
                   dict are preserved (if for example it is an OrderedDict)

    method_01_py3: Python 3 version of method-01-py2
    method_02_py3: Python 3 version of method-02-py3
    method_03_py3: Python 3 version of method-03-py2
    '''

    def __init__(self, option_name=None, short_option='-m', long_option='--method_name',
                 default=mn.method_01_py3, help=help_arg, **kwargs):
        super().__init__(option_name, short_option,
                         long_option, default=default, help=help, **kwargs)


class NumberTimesArgument(Argument):
    def __init__(self):
        self.argument_name = 'number_times'


class NumberItemsArgument(Argument):
    def __init__(self):
        self.argument_name = 'number_items'


class PrecisionArgument(Argument):
    def __init__(self):
        self.argument_name = 'precision'


class UseItemsArgument(Argument):
    def __init__(self):
        self.argument_name = 'use_items'


class UseSetDefaultArgument(Argument):
    def __init__(self):
        self.argument_name = 'use_setdefault'


class SmallTestArgument(Argument):
    def __init__(self):
        self.argument_name = 'small_test'
