import datetime
import json
import os
from pathlib import Path
import shlex
import subprocess
import tempfile

import ipdb

from reverse_dict.argparser_builder import ArgParserBuilder
from reverse_dict.arguments import get_common_arguments, MethodNameArgument, \
    UseItemsArgument, UseSetDefaultArgument
import scripts


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
    list_arguments = [MethodNameArgument(), UseItemsArgument(), UseSetDefaultArgument()]
    list_arguments.extend(get_common_arguments())
    parser_builder = ArgParserBuilder(script_description=script_description,
                                      list_arguments=list_arguments)
    parser = parser_builder.get_parser()
    args = parser.parse_args()

    # Create temp directory & file
    directory = Path(tempfile.gettempdir()) / Path(__file__).stem
    directory.mkdir(exist_ok=True)
    json_file = directory / '{}.{}'.format(str(datetime.datetime.utcnow()).replace(' ', '_'), 'json')
    if not json_file.exists():
        # logger.info("json_file exists: " + str(json_file))
        with json_file.open('w') as f:
            json.dump(args.__dict__, f)

    # Run shell command
    method_module = scripts.scripts_lookup[args.method_name]
    python_version = method_module.python_version
    cmd = "./run_{}_script.py {} {}".format(python_version, args.method_name, json_file)
    # cmd = './run_{}_script.py {}'.format(python_version, options)
    cmd = shlex.split(cmd)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = result.stdout.decode('utf-8')
    print(stdout)

    # Remove temp file
    os.remove(json_file)
