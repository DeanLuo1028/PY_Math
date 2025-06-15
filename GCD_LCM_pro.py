from math import gcd as math_gcd

def gcd(*numbers):
    """計算多個數的最大公因數"""
    from functools import reduce

    # 使用 math.gcd 兩兩計算，reduce會像這樣運作：
    # gcd(12, 18, 24) → gcd(gcd(12, 18), 24) → gcd(6, 24) → 6
    return reduce(math_gcd, numbers)


def lcm(*numbers):
    """計算多個數的最小公倍數"""
    from functools import reduce

    def lcm_two(a, b):
        # lcm(a, b) = a * b // gcd(a, b)
        return a * b // math_gcd(a, b)

    # 兩兩取 lcm，方式與上面一樣
    return reduce(lcm_two, numbers)


# 使用範例
nums = list(map(int, input("請輸入一串整數，用空格分隔：").split()))
print("gcd =", gcd(*nums))
print("lcm =", lcm(*nums))
