import time
import ipdb

from argparser_builder import ArgParserBuilder, Argument, argument_names
from method import Method, method_names as mn
from utils import get_args_from_namespace


class Method01(Method):
    def __init__(self, method_name, **kwargs):
        super().__init__(method_name, **kwargs)

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
    ipdb.set_trace()
    parser_builder \
        = ArgParserBuilder(method_name=mn.method_01_py3,
                           list_arguments=[Argument(argument_names.number_items,
                                                    '-ni', '--number-times',
                                                    default=5, help='test')])
    parser = parser_builder.get_parser()
    args, unknown = parser.parse_known_args()

    print('Args: {}'.format(get_args_from_namespace(args)))
    print('Unknown args: {}'.format(unknown))
    method_01 = Method01(method_name=mn.method_01_py3, **args.__dict__)
    method_01.compute_avg_run_times()
