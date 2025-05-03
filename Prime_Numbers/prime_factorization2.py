def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

prime = [2, 3]
result = [0, 0]
n = int(input("請輸入你要分解的數字: "))
original_n = n
if n == 1:
    result.append(1)

i = 0  # 从第一个质数开始
while True:
    if i >= len(prime):  # 如果当前索引超出质数列表范围，则添加新的质数
        p = prime[-1] + 2  # 从最后一个质数后的下一个奇数开始
        while not is_prime(p):
            p += 2
        prime.append(p)
        result.append(0)
    
    if n % prime[i] == 0:
        result[i] += 1
        n = n // prime[i]
    else:
        i += 1

    if n == 1:
        break

print("質因數分解的結果", original_n, "=", end=" ")
for i in range(len(prime)):
    if result[i] != 0:
        print(prime[i], end="")
        if result[i] > 1:
            print("^", result[i], end="")
        if i != len(prime) - 1:
            print(" × ", end="")
