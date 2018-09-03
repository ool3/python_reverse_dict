import datetime
import json
import os
try:
    from pathlib import Path
except ImportError as e:
    # print(e)
    # print("Python 2 detected. os.path will be used instead.")
    python2 = True
else:
    python2 = False
import shlex
import subprocess
import tempfile

# import ipdb

from reverse_dict.argparser_builder import ArgParserBuilder
from reverse_dict.arguments import get_common_arguments, MethodNameArgument, \
    UseItemsArgument, UseSetDefaultArgument
from reverse_dict.config import cfg
import scripts


if __name__ == '__main__':
    script_description = '''
    %(prog)s v{}

    Computes average running times of different methods of reversing a dict's
    keys and values in Python 2.7 and 3:

        - method 1: makes use of dict comprehension, and your dict must
                    contain unique values
        - method 2: makes use of dict.get(), and your dict doesn't contain
                    unique values
        - method 3: makes use of map(reversed,)

    Github project @ {}
    '''.format(cfg.version, cfg.github_url)
    list_arguments = [MethodNameArgument(), UseItemsArgument(), UseSetDefaultArgument()]
    list_arguments.extend(get_common_arguments())
    parser_builder = ArgParserBuilder(script_description=script_description,
                                      list_arguments=list_arguments)
    parser = parser_builder.get_parser()
    args = parser.parse_args()

    # Create temp directory & JSON file
    # The JSON file stores the arguments for the script to be run with the shell
    # command
    temp_dir_path = tempfile.gettempdir()
    json_filename = '{}.{}'.format(str(datetime.datetime.utcnow()).replace(' ', '_'), 'json')
    if python2:
        cur_filename = os.path.basename(__file__)[:-3]
        directory = os.path.join(temp_dir_path, cur_filename)
        try:
            os.mkdir(directory)
        except OSError as e:
            # print(e)
            pass
        json_file_path = os.path.join(directory, json_filename)
        with open(json_file_path, 'w') as f:
            json.dump(args.__dict__, f)
    else:
        directory = Path(temp_dir_path) / Path(__file__).stem
        directory.mkdir(exist_ok=True)
        json_file_path = directory / json_filename
        with json_file_path.open('w') as f:
            json.dump(args.__dict__, f)

    # Run shell command
    method_module = scripts.scripts_lookup[args.method_name]
    python_version = method_module.python_version
    # TODO: run_{python2, python3}_scripts.py should be in ./scripts
    cmd = "./run_{}_script.py {} {}".format(python_version, args.method_name, json_file_path)
    cmd = shlex.split(cmd)
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.PIPE).decode()
    except subprocess.CalledProcessError as e:
        output = e.output.decode()
    finally:
        print('{}'.format(output))

    # Remove temp file
    os.remove(json_file_path)
