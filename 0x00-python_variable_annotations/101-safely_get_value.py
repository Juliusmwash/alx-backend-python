#!/usr/bin/env python3
"""
Defines a type-annotated function 'safely_get_value'.
"""
from typing import TypeVar, Mapping, Any, Union


# Define a type variable for the default value
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary-like object (Mapping).

    Args:
        dct (Mapping): A dictionary-like object.
        key (Any): The key to look up in the dictionary.
        default (Optional[T], optional): The default value to return
        if the key is not found.
            Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found,
        or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
