#!/usr/bin/env python3
"""
Defines a type-annotated function 'zoom_array'.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on a tuple by repeating each element a specified
    number of times.

    Args:
        lst (Tuple): The input tuple.
        factor (int, optional): The zoom factor, indicating
        how many times each element should be repeated. Defaults to 2.

    Returns:
        List: A new list containing elements from the input tuple,
        where each element is repeated 'factor' times.

    Example:
        >>> my_tuple = (12, 72, 91)
        >>> zoom_2x = zoom_array(my_tuple)
        >>> print(zoom_2x)
        [12, 12, 72, 72, 91, 91]

    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
