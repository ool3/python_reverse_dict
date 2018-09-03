#!/usr/bin/env python3
import json
from pathlib import Path
import sys
# Own modules
import scripts


if __name__ == '__main__':
    method_name = sys.argv[1]
    method_module = scripts.scripts_lookup[method_name]
    json_file = Path(sys.argv[2])
    with json_file.open('r') as f:
        args = json.load(f)
    method_module.run_method(args)
