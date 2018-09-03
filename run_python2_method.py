#!/usr/bin/env python2
import sys
# Own modules
from reverse_dict.argparser_builder import ArgParserBuilder
from reverse_dict.arguments import get_common_arguments, UseItemsArgument
from reverse_dict.config import cfg
import reverse_dict.methods as methods


if __name__ == '__main__':
    method_name = sys.argv[1]
    method_class_name = cfg.methods[method_name]
    method_class = methods.__getattribute__(method_class_name)
    print("Method name: {}".format(method_name))
    unknown = None
    script_description = '''
        %(prog)s v{}

        {}

        Github project @ {}
        '''.format(cfg.version, method_class.__method_description__, cfg.github_url)
    list_arguments = [UseItemsArgument()]
    list_arguments.extend(get_common_arguments())
    parser_builder = ArgParserBuilder(prog=method_class.__method_name__+'.py',
                                      script_description=script_description,
                                      list_arguments=list_arguments)
    parser = parser_builder.get_parser()
    args, unknown = parser.parse_known_args()
    args = args.__dict__
    method = method_class(**args)
    print('Args: {}'.format(args))
    if unknown is None:
        # print('Unused args: {}'.format(method.get_unused_kwargs()))
        pass
    else:
        # print('Unknown args: {}'.format(unknown))
        method.compute_avg_run_time()

