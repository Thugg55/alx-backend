#!/usr/bin/env python3
"""
Defines a function named `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page (int): the current page
        page_size (int): the amount of items in a page
    Returns:
        (tuple): a tuple of the start and end index for the given page
    """
    nextPageS = page * page_size
    return nextPageS - page_size, nextPageS
