import argparse
import textwrap


VERSION = '0.1'

if __name__ == '__main__':
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
        prog='compute_running_times',
        description=textwrap.dedent(description),
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--version', action='version',
                        version='%(prog)s {}'.format(VERSION))

    help_arg = '''\
    Name of the method that reverses a dict:
    method-01: makes use of dict comprehension, and the dict must contain
               unique values
    method-02: makes use of dict.get(), and the dict doesn't contain unique values
    method-03: makes use of map(reversed,), and the type and order of the original
               dict are preserved (if for example it is an OrderedDict)
    '''
    parser.add_argument('-m', '--method-name', default='method-01', help=help_arg)
    parser.add_argument('-n', '--number-times', default=10, type=int, help='')
    parser.add_argument('-i', '--number-items', default=10000, type=int, help='')
    parser.add_argument('-ui', '--use-items', action='store_true', help='')
    parser.add_argument('-s', '--small-test', action='store_true', help='')
    args = parser.parse_args()
