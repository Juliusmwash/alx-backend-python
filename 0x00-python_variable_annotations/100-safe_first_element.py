#!/usr/bin/env python3
"""
Defines a type-annotated function 'safe_first_element'.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a sequence or None if
    the sequence is empty.

    Args:
        lst (Sequence[Any]): Any sequence (list, tuple, etc.) of elements.

    Returns:
        Union[Any, None]: The first element of the sequence or
        None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
