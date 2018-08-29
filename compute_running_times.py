import argparse
import os
import shlex
import subprocess
import textwrap

import ipdb


VERSION = '0.1'
python2_path = '/usr/local/bin/python2.7'
python3_path = os.path.expanduser('~/miniconda3/envs/test_py3/bin/python')

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
        # prog='compute_running_times',
        description=textwrap.dedent(description),
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--version', action='version',
                        version='%(prog)s {}'.format(VERSION))

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
    parser.add_argument('-m', '--method_name', default='method_01_py3', help=help_arg)
    parser.add_argument('-n', '--number_times', default=10, type=int, help='')
    parser.add_argument('-i', '--number_items', default=10000, type=int, help='')
    parser.add_argument('-p', '--precision', default=4, type=int, help='')
    parser.add_argument('-ui', '--use_items', action='store_true', help='')
    parser.add_argument('-usd', '--use_setdefault', action='store_true', help='')
    parser.add_argument('-s', '--small_test', action='store_true', help='')
    args = parser.parse_args()

    options = ''
    which_python = None
    which_method = None
    for k, v in args.__dict__.items():
        if k == 'method_name':
            pos = v.find('_py')
            which_method = v[:pos]
            if v[pos+1:] == 'py3':
                which_python = python3_path
            else:
                which_python = python2_path
        elif isinstance(v, bool):
            options += "--{} ".format(k)
        else:
            options += "--{}={} ".format(k, v)
    options = options.strip()
    assert which_python is not None, "Can't determine which " \
                                     "python version (2 or 3) to use for " \
                                     "running the method's script"

    cmd = '{} {}/{} {}'.format(which_python, which_method, args.method_name+'.py', options)
    cmd = shlex.split(cmd)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = result.stdout.decode('utf-8')
    print(stdout)
