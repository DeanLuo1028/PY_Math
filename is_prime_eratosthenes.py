def is_prime(n):
    is_prime_list = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime_list[i]:
            for j in range(i * i, n + 1, i):
                if j == n: return False # 如果要標記不是質數的剛好就是n，直接回傳False
                is_prime_list[j] = False
    return is_prime_list[n]


for i in range(1001):
    if is_prime(i):
        print(i,sep="", end=", ")