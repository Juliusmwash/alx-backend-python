#!/usr/bin/env python3
"""
Defines a type-annotated function 'zoom_array'.
"""
from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zooms in on a list by repeating each element a specified number of times.

    Args:
        lst (List[int]): The input list of integers.
        factor (int, optional): The zoom factor, indicating how many
        times each element
            should be repeated. Defaults to 2.

    Returns:
        List[int]: A new list containing elements from the input list,
        where each element
        is repeated 'factor' times.

    Example:
        >>> array = [12, 72, 91]
        >>> zoom_2x = zoom_array(array)
        >>> print(zoom_2x)
        [12, 12, 72, 72, 91, 91]

    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
