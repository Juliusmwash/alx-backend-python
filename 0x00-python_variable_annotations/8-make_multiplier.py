#!/usr/bin/env python3
"""
Define a type-annotated function 'make_multiplier'.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to be used by the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the result of multiplying that float by the
        specified multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
