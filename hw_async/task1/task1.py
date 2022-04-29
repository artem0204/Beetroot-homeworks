import asyncio
import multiprocessing
import pprint
import time
from typing import Union


async def fibonacci(num: int) -> int:
    if not isinstance(num, int) and num <= 0:
        raise ValueError("it should be positive number ")
    if num in {0, 1}:
        return num
    previous, fib_number = 0, 1
    for _ in range(2, num + 1):
        previous, fib_number = fib_number, previous + fib_number
    return fib_number


def fibonacci2(num: int) -> int:
    if not isinstance(num, int) and num <= 0:
        raise ValueError("it should be positive number ")
    if num in {0, 1}:
        return num
    previous, fib_number = 0, 1
    for _ in range(2, num + 1):
        previous, fib_number = fib_number, previous + fib_number
    return fib_number


async def factorial(num: int) -> int:
    f = 1
    if num <= 0:
        raise ValueError("it should be positive number")
    else:
        for i in range(2, num + 1):
            f *= i
        return f


def factorial2(num: int) -> int:
    f = 1
    if num <= 0:
        raise ValueError("it should be positive number")
    else:
        for i in range(2, num + 1):
            f *= i
        return f


async def square_num(num: int) -> int:
    if num <= 0:
        raise ValueError("it should be positive number")
    else:
        rez = num * num
        return rez


def square_num2(num: int) -> int:
    if num <= 0:
        raise ValueError("it should be positive number")
    else:
        rez = num * num
        return rez


async def cubic_num(num: int) -> int:
    if num <= 0:
        raise ValueError("it should be positive number")
    else:
        rez = num ** 3
        return rez


def cubic_num2(num: int) -> int:
    if num <= 0:
        raise ValueError("it should be positive number")
    else:
        rez = num ** 3
        return rez


async def main() -> Union[tuple, list]:
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    for num in range(1, 11):
        rez = await asyncio.gather(fibonacci(num), factorial(num), square_num(num), cubic_num(num))
        l1.append(rez[0])
        l2.append(rez[1])
        l3.append(rez[2])
        l4.append(rez[3])
    return l1, l2, l3, l4


def main2() -> Union[tuple, list]:
    with multiprocessing.Pool() as pool:
        rez1 = pool.map_async(fibonacci2, [num for num in range(1, 11)])
        rez2 = pool.map_async(factorial2, [num for num in range(1, 11)])
        rez3 = pool.map_async(square_num2, [num for num in range(1, 11)])
        rez4 = pool.map_async(cubic_num2, [num for num in range(1, 11)])
        return rez1.get(), rez2.get(), rez3.get(), rez4.get()


if __name__ == "__main__":
    time_start = time.time()
    loop = asyncio.get_event_loop().run_until_complete(main())
    time_end = time.time() - time_start
    pprint.pprint(loop)
    print(f"result of time for async: {time_end} ")
    time_start2 = time.time()
    pprint.pprint(main2())
    time_end2 = time.time() - time_start2
    print(f"result of time for function: {time_end2}")

