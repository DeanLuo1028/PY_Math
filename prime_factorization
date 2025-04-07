import math
def Isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

prime = [2,3,0]
result = [0,0]
n = int(input("請輸入你要分解的數字: "))
original_n = n
if n == 1:
    result.append(1)
while True:
    i = 1
    if i > 2:
        prime[i] = 0
        result[i] = 0
    p = 1
    if n%prime[i-1] == 0:
        result[i-1] += 1
        n = n//prime[i-1]
    elif prime[i-1] == 2:
        i += 1
    else:
        #在質數列中添加新的質數
        p = prime[i-1]
        while True:
            if Isprime(p+2):
                p += 2
                break
            else:
                p += 2
        prime[i] = p
        result[i-1] = 0
        i += 1

    if n == 1:
        break

print("質因數分解的結果", original_n, "=", end="")
for i in range(len(prime)):
    if result[i]!= 0:
        print(prime[i], "^", result[i], end="")
        if i != len(prime)-1:
            print(" × ", end="")
print()
exit()