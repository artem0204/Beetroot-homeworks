from typing import Optional
from typing import Union


def to_power(x: Optional[Union[int, float]], exp: int) -> Optional[Union[int, float]]:
    if exp == 1:
        return x
    elif exp <= 0:
        raise ValueError(f"Function cant work with {exp}")
    else:
        return x * to_power(x, exp - 1)



