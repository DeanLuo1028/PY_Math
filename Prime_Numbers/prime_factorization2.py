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

# 初始質數表與次數表
prime = [2, 3]
result = [0, 0]

n = int(input("請輸入你要分解的數字: "))
original_n = n

if n == 1:
    print("1 沒有質因數分解。")
else:
    i = 0
    while n != 1:
        if i >= len(prime):  # 動態補上新質數
            p = prime[-1] + 2
            while not is_prime(p):
                p += 2
            prime.append(p)
            result.append(0)

        if n % prime[i] == 0:
            result[i] += 1
            n //= prime[i]
        else:
            i += 1

    # 格式化輸出結果
    print(f"{original_n} 的質因數分解為：", end="")
    first = True
    for i in range(len(prime)):
        if result[i] != 0:
            if not first:
                print(" × ", end="")
            print(prime[i], end="")
            if result[i] > 1:
                print("^" + str(result[i]), end="")
            first = False
    print()
