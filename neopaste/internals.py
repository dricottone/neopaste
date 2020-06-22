#!/usr/bin/env python3

import sys
from typing import *

VERSION = (1,0,0,)

def _read_stdin() -> Iterator[str]:
    try:
        for line in sys.stdin.readlines():
            yield line.rstrip()
    except KeyboardInterrupt:
        sys.stdout.write("\n")

def _read_file(filename: str) -> Iterator[str]:
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                yield line.rstrip()
    except OSError:
        _print_invalid_file(filename)

def _read_files(filenames: List[str]) -> List[List[str]]:
    contents = list()
    if len(filenames) == 0:
        contents.append(list(_read_stdin()))
    else:
        for filename in filenames:
            if filename == '-':
                contents.append(list(_read_stdin()))
            else:
                contents.append(list(_read_file(filename)))
    return contents

def _print_help() -> None:
    _msg = (
        "Usage: npaste [OPTIONS] [FILE..]",
        "neopaste - Paste file streams side-by-side",
        "Options:",
        "  -c, --center                 center the columns",
        "  -d DELIM, --delimiter DELIM  delimit columns with DELIM",
        "  -l, --left                   left-justify the columns [Default]",
        "  -r, --right                  right-justify the columns",
        "  -h, -x, --help               print this message",
        "  -v, -V, --version            print version",
        "If FILE is -, or if no FILEs, read from STDIN.",
    )
    sys.stderr.write("\n".join(_msg) + "\n")

def _print_version() -> None:
    _msg = (
        "npaste {0}".format(".".join(str(v) for v in VERSION)),
    )
    sys.stderr.write("\n".join(_msg) + "\n")

def _print_usage() -> None:
    _msg = (
        "Usage: npaste [OPTIONS] [FILE..]",
    )
    sys.stderr.write("\n".join(_msg) + "\n")

