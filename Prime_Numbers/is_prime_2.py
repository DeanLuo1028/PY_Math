# 這不行
def is_prime(x):
    def inxer_is_prime(x, primes):
        if x==2 or x==3:
            return True
        # 只檢查比 x 的平方根小的質數
        sqrt = int(x ** 0.5) + 1
        for p in primes:
            if p > sqrt:
                return True
            if x % p == 0:
                return False
        return True

    primes = [2]
    for i in range(3, x, 2):  # 只檢查奇數
        if inxer_is_prime(i, primes):
            primes.append(i)
    return x in primes


for i in range(101):
    print(i, end="")
    if is_prime(i):
        print(i,sep="", end=", ")