import asyncio
from time import perf_counter

"""
task: 
How to use async/await to implement the following output:
Even number: 0
Odd number: 1
...
Odd number: 9

Hint:
Define async functions for printing even and odd numbers.
Use asyncio to schedule and run both tasks concurrently.
"""

async def print_even():
    for i in range(0, 10, 2):
        print(f"Even number: {i}")
        await asyncio.sleep(1)

async def print_odd():
    for i in range(1, 10, 2):
        print(f"Odd number: {i}")
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(print_even(), print_odd())

if __name__ == "__main__":
    start_time = perf_counter()
    asyncio.run(main())
    end_time = perf_counter()
    print(f"Time taken: {end_time - start_time:.2f} seconds")   

