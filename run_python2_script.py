#!/usr/bin/env python2
import json
import sys
#import ipdb
# Own modules
import scripts


if __name__ == '__main__':
    method_name = sys.argv[1]
    method_module = scripts.scripts_lookup[method_name]
    with open(sys.argv[2], 'r') as f:
        args = json.load(f)
    #ipdb.set_trace()
    method_module.run_method(args)
