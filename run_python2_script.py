#!/usr/bin/env python2
import sys

import scripts


if __name__ == '__main__':
    method_module = scripts.scripts_lookup[sys.argv[1]]
    method_module.run_method(args)