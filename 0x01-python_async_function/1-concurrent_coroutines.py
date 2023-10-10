#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine 'wait_n'
"""
import asyncio
from typing import List
# Import the wait_random coroutine from the previous file
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with
    the specified max_delay and returns a list of delays in
    ascending order.

    Args:
        n (int): The number of times to run wait_random.
        max_delay (int): The maximum delay in seconds for each
        wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    results = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    results.sort()
    return results
