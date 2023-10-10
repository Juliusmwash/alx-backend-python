#!/usr/bin/env python3
"""
This module defines the function 'task_wait_n'
"""
import asyncio
from typing import List, Any
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n
    times with the specified max_delay and returns a list
    of delays in ascending order.

    Args:
        n (int): The number of times to run task_wait_random.
        max_delay (int): The maximum delay in seconds for each
        task_wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks: List[asyncio.Task] = []

    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    results = await asyncio.gather(*tasks)

    return sorted(results)
