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
    UseItemsArgument
from reverse_dict.config import cfg
import reverse_dict.methods as methods


if __name__ == '__main__':
    script_description = '''
    %(prog)s v{}

    Computes average running times of different methods of reversing a dict's
    keys and values in Python 2.7 and 3:

        - method 1: makes use of dict comprehension, and the dict must contain 
                    unique values
        - method 2: the dictionary doesn't contain unique values and saves all the 
                    keys with the same values in a list
        - method 3: makes use of map(reversed,), useful when the type and order of 
                    the original dictionary must be preserved (e.g. OrderedDict)

    Github project @ {}
    '''.format(cfg.version, cfg.github_url)
    list_arguments = [MethodNameArgument(), UseItemsArgument()]
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
    # TODO: add as first argument to run_python{2,3}_method.py the `
    # method_name` without short and long options so you won't have to add it
    # again as the first option of the shell command
    cmd = "./run_{}_method.py {} {}".format(python_version, args.method_name,
                                            options)
    cmd = shlex.split(cmd)
    subprocess.call(cmd)
    # TODO: Slower code since you have to wait for all the results to generate
    # from the launched script. But it takes a little bit longer when using
    # the supposedly better solution `subprocess.call(cmd)`, where you get the
    # results in real-time. Why is it so?
    """
    print("Shell command executed and waiting on results...")
    print("...waiting...waiting...waiting...waiting...")
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.PIPE).decode()
    except subprocess.CalledProcessError as e:
        output = e.output.decode()
    finally:
        print('{}'.format(output))
    """
