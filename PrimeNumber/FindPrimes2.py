# 生成前n個質數
import math
def is_prime(n, p):
    isPrime = True
    for j in range(0, len(p)): # 遍歷之前找到的質數
        # 若之前找到的質數大於i的平方根，則不用再檢查
        if p[j] > math.sqrt(n): break # n是質數
        elif n % p[j] == 0: # 若n能被之前找到的質數整除，則i不是質數
            isPrime = False
            break
    return isPrime
"""
根據質數定理，每個質數都可以用6k-1或6k+1表示，因此我們可以用這個方法找出更多的質數。
"""
def find_primes(n):
    p = [2, 3] # 先加入質數2, 3
    i = 1
    while True:
        x = 6*i - 1
        if is_prime(x, p): p.append(x)
        # 若找到了n個質數，則停止
        if len(p) >= n: break
        x = 6*i + 1
        if is_prime(x, p): p.append(x)
        # 若找到了n個質數，則停止
        if len(p) >= n: break
        i += 1
    return p
    
p = find_primes(1000)
print(p)