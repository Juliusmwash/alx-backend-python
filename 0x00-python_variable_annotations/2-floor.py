#!/usr/bin/env python3
"""
This module defines a type-annotated function 'floor'.
"""
import math


def floor(n: float) -> int:
    """
    A type-annotated function floor which takes a float as an argument and
    returns the floor of the float.
    Args:
        n(float) - type-annotated argument.
    """
    return math.floor(n)
