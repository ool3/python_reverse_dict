import argparse
import textwrap


class ArgParserBuilder:
    def __init__(self, prog, script_description='', list_arguments=[]):
        self.prog = prog
        self.script_description = script_description
        self.list_arguments = list_arguments
        self.parser = self._get_arg_parser()

    def get_parser(self):
        return self.parser

    def _get_arg_parser(self):
        parser = argparse.ArgumentParser(
            prog=self.prog,
            description=textwrap.dedent(self.script_description),
            formatter_class=argparse.RawTextHelpFormatter)
        self._add_arguments(parser)
        return parser

    def _add_arguments(self, parser):
        for arg in self.list_arguments:
            parser.add_argument(*arg.args, **arg.kwargs)
