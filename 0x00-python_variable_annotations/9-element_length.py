#!/usr/bin/env python3
"""
Defines a type-annotated function 'element_length'
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable of
    sequences (e.g., strings, lists and return a list of tuples,
    where each tuple contains the original sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences
        (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: List of tuples where each
        tuple contains a sequence from the input iterable and its
        corresponding length as an integer.
    """
    return [(i, len(i)) for i in lst]
