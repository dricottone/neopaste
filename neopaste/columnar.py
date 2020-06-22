#!/usr/bin/env python3

import re
import itertools
from typing import List, Tuple, Iterator

REGEX_MATCH = re.compile(r'\x1b[^m]*m')
REGEX_SPLIT = re.compile(r'(\x1b[^m]*m)')

def _uncolored_length(s: str) -> str:
    """Remove ANSI codes from string s."""
    return len(REGEX_MATCH.sub('', s))

def _spaces(n: int) -> str:
    """Return a string of N spaces."""
    if n > 0:
        return " " * n
    else:
        return ""

def _max_length(items: List) -> int:
    """Find length of longest item within an item's contents."""
    length = 0
    for item in items:
        if isinstance(item, str):
            _len = _uncolored_length(item)
        else:
            _len = len(item)
        if _len > length:
            length = _len
    return length

def _ljust(width: int, items: List[str], *, length: int = 0) -> Iterator[str]:
    """Iterate over left-justified lines within a file's contents."""
    for item in items:
        length -= 1
        yield item + _spaces(width - _uncolored_length(item))
    if length > 0:
        for _ in range(length):
            yield _spaces(width)


def _rjust(width: int, items: List[str], *, length: int = 0) -> Iterator[str]:
    """Iterate over right-justified lines within a file's contents."""
    for item in items:
        length -= 1
        yield _spaces(width - _uncolored_length(item)) + item
    if length > 0:
        for _ in range(length):
            yield _spaces(width)

def _center(width: int, items: List[str], *, length: int = 0) -> Iterator[str]:
    """Iterate over centered lines within a file's contents."""
    for item in items:
        length -= 1
        _width = width - _uncolored_length(item)
        _pre = _width // 2
        _post = _width - _pre
        yield _spaces(_pre) + item + _spaces(_post)
    if length > 0:
        for _ in range(length):
            yield _spaces(width)

def _column_widths(
    contents: List[List[str]],
) -> Iterator[int]:
    """Iterate over column lengths, computed from a list of file contents."""
    for items in contents:
        yield _max_length(items)

def ljust_columns(
    contents: List[List[str]],
) -> Iterator[List[str]]:
    """Iterate over lines containing left-justified columns, built from a list
    of file contents (each to a row).
    """
    _height = _max_length(contents)
    _widths = _column_widths(contents)
    _cols = [_ljust(w, c, length=_height) for w,c in zip(_widths, contents)]
    _rows = zip(*_cols)
    yield from _rows

def rjust_columns(
    contents: List[List[str]],
) -> Iterator[List[str]]:
    """Iterate over lines containing right-justified columns, built from a list
    of file contents (each to a row).
    """
    _height = _max_length(contents)
    _widths = _column_widths(contents)
    _cols = [_rjust(w, c, length=_height) for w,c in zip(_widths, contents)]
    _rows = zip(*_cols)
    yield from _rows

def center_columns(
    contents: List[List[str]],
) -> Iterator[List[str]]:
    """Iterate over lines containing centered columns, built from a list of
    file contents (each to a row).
    """
    _height = _max_length(contents)
    _widths = _column_widths(contents)
    _cols = [_center(w, c, length=_height) for w,c in zip(_widths, contents)]
    _rows = zip(*_cols)
    yield from _rows

