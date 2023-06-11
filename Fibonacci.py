import asyncio
import random


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


async def async_fib(n):
    await asyncio.sleep(random.uniform(0, 1))
    return fib(n)


async def main():
    n = int(input("Enter a positive number: "))
    task1 = asyncio.create_task(async_fib(n))
    task2 = asyncio.create_task(async_fib(n))

    tasks = [task1, task2]
    finished, _unfinished = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    finished = finished.pop()