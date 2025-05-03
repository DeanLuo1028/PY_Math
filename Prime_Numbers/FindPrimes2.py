# 生成所有小於等於n的質數
# 使用試除法
def is_prime(n, primes):
    # 只檢查比 n 的平方根小的質數
    sqrt = int(n ** 0.5) + 1
    for prime in primes:
        if prime > sqrt:
            return True
        if n % prime == 0:
            return False
    return True

def find_primes(limit):
    primes = [2]
    for n in range(3, limit, 2):  # 只檢查奇數
        if is_prime(n, primes): primes.append(n)
    return primes


# 測試執行時間
import timeit

def test():
    find_primes(100000)

# 重複執行 5 次，每次執行函式 1000 次，取平均時間
time_taken = timeit.timeit(test, number=1000)
print(f"平均每次執行花費：{time_taken / 1000:.8f} 秒")