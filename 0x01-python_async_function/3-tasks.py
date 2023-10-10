#!/usr/bin/env python3
"""
This module defines the function 'task_wait_random'
"""
import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[Any]:
    """
    Create and return an asyncio.Task that runs the wait_random
    coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for
        wait_random.

    Returns:
        asyncio.Task: An asyncio.Task representing the execution
        of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
