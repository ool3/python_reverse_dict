import os
import shlex
import subprocess

import ipdb

from reverse_dict.argparser_builder import ArgParserBuilder
from reverse_dict.arguments import get_common_arguments, MethodNameArgument, \
    UseItemsArgument, UseSetDefaultArgument


VERSION = '0.1'
GITHUB_URL = 'https://github.com/raul23/python_reverse_dict'
python2_path = '/usr/local/bin/python2.7'
python3_path = os.path.expanduser('~/miniconda3/envs/test_py3/bin/python')


if __name__ == '__main__':
    script_description = '''
    %(prog)s v{}

    Computes average running times of different methods of reversing a dict's
    keys and values:

        - method 1: makes use of dict comprehension, and your dict must
                    contain unique values
        - method 2: makes use of dict.get(), and your dict doesn't contain
                    unique values
        - method 3: makes use of map(reversed,)

    Github project @ {}
    '''.format(VERSION, GITHUB_URL)
    ipdb.set_trace()
    list_arguments = [MethodNameArgument(), UseItemsArgument(), UseSetDefaultArgument()]
    list_arguments.extend(get_common_arguments())
    parser_builder = ArgParserBuilder(script_description=script_description,
                                      list_arguments=list_arguments)
    parser = parser_builder.get_parser()
    args = parser.parse_args()

    options = ''
    which_python = None
    method_dirname = None
    for k, v in args.__dict__.items():
        if v is False:
            continue
        elif v is True:
            options += "--{} ".format(k)
        else:
            options += "--{}={} ".format(k, v)
        if k == 'method_name':
            pos = v.find('_py')
            method_dirname = v[:pos]
            if v[pos+1:] == 'py3':
                which_python = python3_path
            else:
                which_python = python2_path
    ipdb.set_trace()
    options = options.strip()
    assert which_python is not None, "Can't determine which " \
                                     "python version (2 or 3) to use for " \
                                     "running the method's script"

    cmd = '{} {}/{} {}'.format(which_python, method_dirname, args.method_name+'.py', options)
    ipdb.set_trace()
    cmd = shlex.split(cmd)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = result.stdout.decode('utf-8')
    print(stdout)
