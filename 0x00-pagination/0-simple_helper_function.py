#!/usr/bin/env python3
'''
a function named index_range that takes two integer
arguments page and page_size.
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''
    return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list
    for those particular pagination parameters
    '''
    offset = page * page_size
    return (offset - page_size, offset)
