#!/usr/bin/env python2
import os
import sys

# TODO: add this into env variable
sys.path.insert(0, os.path.expanduser("~/PycharmProjects/github_projects/python_reverse_dict"))
from reverse_dict.argparser_builder import ArgParserBuilder
from reverse_dict.arguments import UseItemsArgument, get_common_arguments
from reverse_dict.config import cfg
from reverse_dict.methods import Method01Py2


method_name = Method01Py2.__method_name__
python_version = Method01Py2.__python_version__


def run_method(args=None):
    unknown = None
    if args is None:
        # TODO: use Argument.{short_option, long_option} instead of `-ui` and `--use_items`
        # in the script description
        script_description = '''
        %(prog)s v{}
    
        %(prog)s works with Python 2 by reversing a dict's keys and values using a dict
        comprehension, and assumes that the dict contains UNIQUE values. Also, by
        default dict.iteritems() is used when populating the reversed dict. Use the
        option -ui, --use_items to instead use dict.items() which is less efficient.
    
        Github project @ {}
        '''.format(cfg.version, Method01Py2.__method_name__, cfg.github_url)
        list_arguments = [UseItemsArgument()]
        list_arguments.extend(get_common_arguments())
        parser_builder = ArgParserBuilder(script_description=script_description,
                                          list_arguments=list_arguments)
        parser = parser_builder.get_parser()
        args, unknown = parser.parse_known_args()
        args = args.__dict__
    method_01 = Method01Py2(**args)
    print('Args: {}'.format(args))
    if unknown is None:
        print('Unused args: {}'.format(method_01.get_unused_kwargs()))
    else:
        print('Unknown args: {}'.format(unknown))
    method_01.compute_avg_run_time()


if __name__ == '__main__':
    run_method()
