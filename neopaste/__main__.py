#!/usr/bin/env python3

import sys

from . import cli
from . import internals
from . import columnar

def main():
    _config, _positionals = cli.main(sys.argv[1:])

    if "version" in _config.keys():
        internals._print_version()
        sys.exit(0)
    elif "help" in _config.keys():
        internals._print_help()
        sys.exit(0)

    if "left" in _config.keys():
        process = columnar.ljust_columns
    elif "right" in _config.keys():
        process = columnar.rjust_columns
    elif "center" in _config.keys():
        process = columnar.center_columns
    else:
        process = columnar.ljust_columns

    _delimiter = _config.get("delimiter", "\t")

    contents = internals._read_files(_positionals)

    for line in process(contents):
        sys.stdout.write(_delimiter.join(line) + "\n")

    sys.exit(0)

if __name__ == "__main__":
    main()

