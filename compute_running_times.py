import os
import shlex
import subprocess

import ipdb

from argparser_builder import ArgParserBuilder
from method import method_names as mn


VERSION = '0.1'
python2_path = '/usr/local/bin/python2.7'
python3_path = os.path.expanduser('~/miniconda3/envs/test_py3/bin/python')

if __name__ == '__main__':
    parser_builder = ArgParserBuilder(method_name=mn.main_script)
    parser = parser_builder.parser
    args = parser.parse_args()

    options = ''
    which_python = None
    which_method = None
    ipdb.set_trace()
    for k, v in args.__dict__.items():
        if v is False:
            continue
        elif v is True:
            options += "--{} ".format(k)
        else:
            options += "--{}={} ".format(k, v)
        if k == 'method_name':
            pos = v.find('_py')
            which_method = v[:pos]
            if v[pos+1:] == 'py3':
                which_python = python3_path
            else:
                which_python = python2_path
    ipdb.set_trace()
    options = options.strip()
    assert which_python is not None, "Can't determine which " \
                                     "python version (2 or 3) to use for " \
                                     "running the method's script"

    cmd = '{} {}/{} {}'.format(which_python, which_method, args.method_name+'.py', options)
    ipdb.set_trace()
    cmd = shlex.split(cmd)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = result.stdout.decode('utf-8')
    print(stdout)
