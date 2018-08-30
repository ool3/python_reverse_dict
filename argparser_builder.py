import argparse
import textwrap

from method import method_names as mn


VERSION = '0.1'


class ArgParserBuilder:
    def __init__(self, method_name):
        self.method_name = method_name
        self.parser = self._get_arg_parser()
        self.arguments = Arguments(self.parser)

    def _get_arg_parser(self):
        if self.method_name == mn.main_script:
            return self._get_main_parser()
        elif self.method_name in mn.get_01_methods():
            return self._get_method_01_parser()
        elif self.method_name in mn.get_02_methods():
            return self._get_method_02_parser()
        elif self.method_name in mn.get_03_methods():
            return self._get_method_03_parser()

    def _get_main_parser(self):
        description = '''
                %(prog)s v{}
    
                Computes average running times of different methods of reversing a dict
                    - method 1: makes use of dict comprehension, and your dict must
                                contain unique values
                    - method 2: makes use of dict.get(), and your dict doesn't contain
                                unique values
                    - method 3: makes use of map(reversed,)
    
                Github project @ https://github.com/raul23/python_reverse_dict
                '''.format(VERSION)
        parser = argparse.ArgumentParser(
            # prog='compute_running_times',
            description=textwrap.dedent(description),
            formatter_class=argparse.RawTextHelpFormatter)
        self.arguments.add_all_arguments()
        return parser

    def _get_method_01_parser(self):
        description = ''
        parser = argparse.ArgumentParser(
            # prog='compute_running_times',
            description=textwrap.dedent(description),
            formatter_class=argparse.RawTextHelpFormatter)
        self.arguments.add_common_arguments()
        return parser

    def _get_method_02_parser(self):
        description = ''
        parser = argparse.ArgumentParser(
            # prog='compute_running_times',
            description=textwrap.dedent(description),
            formatter_class=argparse.RawTextHelpFormatter)
        self.arguments.add_common_arguments()
        return parser

    def _get_method_03_parser(self):
        description = ''
        parser = argparse.ArgumentParser(
            # prog='compute_running_times',
            description=textwrap.dedent(description),
            formatter_class=argparse.RawTextHelpFormatter)
        self.arguments.add_common_arguments()
        return parser


class Arguments:
    def __init__(self, parser):
        self.parser = parser

    def add_method_name_argument(self):
        help_arg = help_arg = '''\
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
        self.parser.add_argument('-m', '--method_name', default=mn.method_02_py2, help=help_arg)

    def add_number_times_argument(self):
        help_arg = ''
        self.parser.add_argument('-n', '--number_times', default=10, type=int, help=help_arg)

    def add_number_items_argument(self):
        help_arg = ''
        self.parser.add_argument('-i', '--number_items', default=10000, type=int, help=help_arg)

    def add_precision_argument(self):
        help_arg = ''
        self.parser.add_argument('-p', '--precision', default=4, type=int, help=help_arg)

    def add_use_items_argument(self):
        help_arg = ''
        self.parser.add_argument('-ui', '--use_items', action='store_true', help=help_arg)

    def add_use_default_argument(self):
        help_arg = ''
        self.parser.add_argument('-usd', '--use_setdefault', action='store_true', help=help_arg)

    def add_small_test_argument(self):
        hel_arg= ''
        self.parser.add_argument('-s', '--small_test', action='store_true', help='')

    def add_common_arguments(self):
        self.add_method_name_argument()
        self.add_number_times_argument()
        self.add_number_items_argument()
        self.add_precision_argument()
        self.add_small_test_argument()

    def add_all_arguments(self):
        for k, v in self.__dict__.items:
            if k.startswith('add_') and k.endswith('_argument'):
                add_argument = self.__getattribute__(k)
                add_argument()
