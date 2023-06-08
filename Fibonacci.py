import asyncio
import random


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


async def async_fib(n):
    await asyncio.sleep(random.random())  # Introduce random delay
    return fib(n)


async def main():
    n = int(input("Enter a positive number: "))
    task1 = asyncio.create_task(async_fib(n))
    task2 = asyncio.create_task(async_fib(n))
    await asyncio.gather(task1, task2)  # Wait for both tasks to finish
    result1 = task1.result()
    result2 = task2.result()

    print(f"Fibonacci number Fib({n}): {result1}")
    if result1 == result2:
        print("Both tasks finished at the same time.")
    elif result1 < result2:
        print("Task 1 finished first.")
    else:
        print("Task 2 finished first.")


if __name__ == "__main__":
    asyncio.run(main())
