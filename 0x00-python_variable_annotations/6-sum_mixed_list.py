#!/usr/bin/env python3
"""
This module defines a type-annotated function 'sum_mixed_list'.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): List of integers and floats.

    Returns:
        float: The sum of the integers and floats in the list.
    """
    total_sum: float = sum(mxd_lst)
    return float(total_sum)
