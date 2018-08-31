#!/usr/bin/env python3
import os
import sys

# import ipdb

# TODO: add this into env variable
sys.path.insert(0, os.path.expanduser("~/PycharmProjects/github_projects/python_reverse_dict"))
from reverse_dict.argparser_builder import ArgParserBuilder
from reverse_dict.arguments import get_common_arguments
from reverse_dict.config import cfg
from reverse_dict.methods import Method02Py3


method_name = Method02Py3.__method_name__
python_version = Method02Py3.__python_version__


def run_method(args=None):
    unknown = None
    if args is None:
        script_description = '''
        %(prog)s v{}

        %(prog)s works on Python 3 by reversing a dict's keys and values. It
        saves all the keys associated with the same values in a list. It makes
        use of dict.get() by default when populating the reversed dict, and
        assumes that the dict contains NON-UNIQUE values.

        Github project @ {}
        '''.format(cfg.version, Method02Py3.__method_name__, cfg.github_url)
        list_arguments = get_common_arguments()
        parser_builder = ArgParserBuilder(script_description=script_description,
                                          list_arguments=list_arguments)
        parser = parser_builder.get_parser()
        args, unknown = parser.parse_known_args()
        args = args.__dict__
    method_02 = Method02Py3(**args)
    print('Args: {}'.format(args))
    if unknown is None:
        print('Unused args: {}'.format(method_02.get_unused_kwargs()))
    else:
        print('Unknown args: {}'.format(unknown))
    method_02.compute_avg_run_time()


if __name__ == '__main__':
    run_method()