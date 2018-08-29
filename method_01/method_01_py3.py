import argparse
import time
import ipdb


def method_01(**kwargs):
    number_times = kwargs['number_times']
    number_items = kwargs['number_items']
    decimal_precision = kwargs['precision']
    if kwargs['small_test']:
        number_times = 1
        number_items = 1
        my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
    else:
        my_dict = dict(zip(range(1, number_items + 1), range(-number_items, 0)))
    inv_dict = {}
    durations = 0
    count = 1
    for i in range(number_times):
        start_time = time.time()
        inv_dict = {v: k for k, v in my_dict.items()}
        duration = time.time() - start_time
        durations += duration
        print('#{} Duration: {:.{}f}'.format(count, duration, decimal_precision))
        count += 1

    print('Avg: {:.{}f} seconds'.format((durations / number_items), decimal_precision))
    if kwargs['small_test']:
        print(my_dict)
        print(inv_dict)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number_times', default=10, type=int, help='')
    parser.add_argument('-i', '--number_items', default=10000, type=int, help='')
    parser.add_argument('-p', '--precision', default=4, type=int, help='')
    parser.add_argument('-s', '--small_test', action='store_true', help='')
    args, unknown = parser.parse_known_args()

    method_01(**args.__dict__)
