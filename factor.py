import math
from typing import Generator, List

def factor(n: int) -> List[int]:
    """
    回傳 n 的所有正因數，並以升序排列。

    參數：
        n (int): 正整數

    回傳：
        List[int]: n 的所有正因數，已排序。
    
    例外：
        TypeError: 若 n 不是整數。
        ValueError: 若 n <= 0。
    """
    if not isinstance(n, int):
        raise TypeError("請傳入正整數！")
    if n <= 0:
        raise ValueError("請傳入正整數！")
    if n == 1:
        return [1]
    
    factors: set[int] = set()
    step = 1 if n & 1 == 0 else 2

    for i in range(1, math.isqrt(n) + 1, step):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)


def factor_gen(n: int) -> Generator[int, None, None]:
    """
    產生器：依升序產生 n 的所有正因數（速度快、順序正確，僅需暫存一部分因數）。

    參數：
        n (int): 正整數

    產生：
        int: n 的一個因數（由小到大）
    
    例外：
        TypeError: 若 n 不是整數。
        ValueError: 若 n <= 0。
    """
    if not isinstance(n, int):
        raise TypeError("請傳入正整數！")
    if n <= 0:
        raise ValueError("請傳入正整數！")
    yield 1
    if n == 1:
        return

    big_factors: List[int] = []
    sqrt_n = math.isqrt(n)

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            yield i
            if i != n // i:
                big_factors.append(n // i)

    for i in reversed(big_factors):
        yield i
    yield n


def factor_gen2(n: int) -> Generator[int, None, None]:
    """
    產生器：依發現順序產生 n 的所有正因數（速度快、最省記憶體，但順序不保證）。

    參數：
        n (int): 正整數

    產生：
        int: n 的一個因數（順序不保證）
    
    例外：
        TypeError: 若 n 不是整數。
        ValueError: 若 n <= 0。
    """
    if not isinstance(n, int):
        raise TypeError("請傳入正整數！")
    if n <= 0:
        raise ValueError("請傳入正整數！")
    yield 1
    if n == 1:
        return

    sqrt_n = math.isqrt(n)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i

    yield n


def factor_gen_sorted(n: int) -> Generator[int, None, None]:
    """
    產生器：依升序產生 n 的所有正因數（順序正確但效率最低，會檢查所有小於 n 的整數）。

    參數：
        n (int): 正整數

    產生：
        int: n 的一個因數（由小到大）
    
    例外：
        TypeError: 若 n 不是整數。
        ValueError: 若 n <= 0。
    """
    if not isinstance(n, int):
        raise TypeError("請傳入正整數！")
    if n <= 0:
        raise ValueError("請傳入正整數！")
    yield 1
    if n == 1:
        return

    if n % 2 == 0:
        for i in range(2, n):
            if n % i == 0:
                yield i
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                yield i
    yield n

if __name__ == '__main__':
    print(factor(12345678987654321))