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
# Own modules
from reverse_dict.argparser_builder import ArgParserBuilder
from reverse_dict.arguments import get_common_arguments, MethodNameArgument, \
    UseItemsArgument, UseSetDefaultArgument
from reverse_dict.config import cfg
import reverse_dict.methods as methods


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
    list_arguments = [MethodNameArgument(), UseItemsArgument(),
                      UseSetDefaultArgument()]
    list_arguments.extend(get_common_arguments())
    parser_builder = ArgParserBuilder(prog=__file__,
                                      script_description=script_description,
                                      list_arguments=list_arguments)
    parser = parser_builder.get_parser()
    args = parser.parse_args()

    # Use dict.iteritems() if Python2, else use dict.items()
    args_items = args.__dict__.iteritems() if python2 else args.__dict__.items()

    options = ''
    for k, v in args_items:
        if isinstance(v, bool):
            if v is True:
                options += '--{} '.format(k)
        else:
            options += '--{}={} '.format(k, v)
    options = options.strip()

    # Run shell command
    method_class_name = cfg.methods[args.method_name]
    method_class = methods.__getattribute__(method_class_name)
    python_version = method_class.__python_version__
    cmd = "./run_{}_method.py {} {}".format(python_version, args.method_name, options)
    cmd = shlex.split(cmd)
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.PIPE).decode()
    except subprocess.CalledProcessError as e:
        output = e.output.decode()
    finally:
        print('{}'.format(output))
