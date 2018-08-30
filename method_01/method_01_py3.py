import argparse
import time
import ipdb

from method import Method
from utils import get_args_from_namespace


class Method01(Method):
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
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--method_name', default='method_01_py3', help='')
    parser.add_argument('-n', '--number_times', default=10, type=int, help='')
    parser.add_argument('-i', '--number_items', default=10000, type=int, help='')
    parser.add_argument('-p', '--precision', default=4, type=int, help='')
    parser.add_argument('-s', '--small_test', action='store_true', help='')
    args, unknown = parser.parse_known_args()

    ipdb.set_trace()

    print('Args: {}'.format(get_args_from_namespace(args)))
    print('Unknown args: {}'.format(unknown))
    method_01 = Method01(**args.__dict__)
    method_01.compute_avg_run_times()
