#!/usr/bin/env python3
"""
Defines a type-annotated function 'sum_list'.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats as argument and returns their sum as a float.
    """
    sum_float: float = sum(num for num in input_list)
    return sum_float
