from typing import Optional


def mult(a: int, n: int) -> int:
    if n == 0:
        return 0
    elif n < 0:
        raise ValueError(f"Cannot multiple on {n} ")
    elif n == 1:
        return a
    else:
        return a + mult(a,n-1)
