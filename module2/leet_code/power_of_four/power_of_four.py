from math import log


def isPowerOfFour(n: int) -> bool:
    return n > 0 and log(n, 4).is_integer()
