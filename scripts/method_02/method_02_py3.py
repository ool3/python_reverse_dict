import argparse
import sys
import time
import ipdb


def method_02(**kwargs):
    number_times = kwargs['number_times']
    number_items = kwargs['number_items']
    decimal_precision = kwargs['precision']
    ipdb.set_trace()
    if kwargs['small_test']:
        number_times = 1
        number_items = 1
        my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'd', 6: 'c'}
    else:
        my_dict = dict(zip(range(1, int(number_items/2)+1), range(-int(number_items/2)+1, 0)))
        my_dict.update(dict(zip(range(int(number_items/2)+1, number_items+1), range(-int(number_items/2)+1, 0))))
    inv_dict = {}
    durations = 0
    count = 1
    for i in range(number_times):
        start_time = time.time()
        inv_dict = {}
        for k, v in my_dict.items():
            inv_dict[v] = inv_dict.get(v, [])
            inv_dict[v].append(k)
        duration = time.time() - start_time
        durations += duration
        print('#{} Duration: {:.{}f}'.format(count, duration, decimal_precision))
        count += 1

    print('Avg: {:.{}f} seconds'.format((durations / number_items),
                                        decimal_precision))
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

    print('Args: {}'.format(sys.argv[1:].__str__()))
    method_02(**args.__dict__)