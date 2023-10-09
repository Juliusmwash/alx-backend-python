#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay seconds (inclusive).

    Args:
        max_delay (float, optional): The maximum delay in
        seconds (inclusive). Defaults to 10.

    Returns:
        float: The random delay that was waited for.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
