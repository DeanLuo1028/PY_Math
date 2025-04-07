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

p = find_primes(1000)
print(p)