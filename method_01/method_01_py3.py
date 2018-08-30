import os
import sys
import time
import ipdb

sys.path.insert(0, os.path.expanduser("~/PycharmProjects/github_projects/python_reverse_dict"))
from argparser_builder import ArgParserBuilder, get_common_arguments
from method import Method
from method_names import method_names as mn
from utils import get_args_from_namespace

VERSION = 0.1
GITHUB_URL = 'https://github.com/raul23/python_reverse_dict'


class Method01(Method):
    __method_name__ = mn.method_01_py3

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def compute_avg_run_times(self):
        count = 1
        for i in range(self.number_times):
            start_time = time.time()
            self.inv_dict = {v: k for k, v in self.my_dict.items()}
            duration = time.time() - start_time
            self.durations += duration
            self.print_duration(count, duration)
            count += 1

        self.print_avg_run_times()
        if self.small_test:
            print(self.my_dict)
            print(self.inv_dict)


if __name__ == '__main__':
    script_description = '''
    %(prog)s v{}

    %(prog)s works on Python 3 by reversing a dict's keys and values using a dict comprehension,
    and assumes that the dict contains UNIQUE values.

    Github project @ {}
    '''.format(VERSION, mn.method_01_py3, GITHUB_URL)
    list_arguments = get_common_arguments()
    parser_builder = ArgParserBuilder(method_name=mn.method_01_py3,
                                      script_description=script_description,
                                      list_arguments=list_arguments)
    parser = parser_builder.get_parser()
    args, unknown = parser.parse_known_args()

    print('Args: {}'.format(get_args_from_namespace(args)))
    print('Unknown args: {}'.format(unknown))
    method_01 = Method01(**args.__dict__)
    method_01.compute_avg_run_times()
