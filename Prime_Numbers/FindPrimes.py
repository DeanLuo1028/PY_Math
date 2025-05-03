# 生成所有小於等於n的質數
# 使用篩法
def is_prime(n, p):
    for j in range(0, len(p)): # 遍歷之前找到的質數
        # 若之前找到的質數大於i的平方根，則不用再檢查
        if p[j] > int(n ** 0.5) + 1: break # n是質數
        elif n % p[j] == 0: # 若n能被之前找到的質數整除，則i不是質數
            return False
    return True

def find_primes(n):
    prime = []
    # 先將每個數字標記為非質數
    p = [True for _ in range(n+1)] # range(n+1)表示0到n的整數
    p[0] = p[1] = False # 0和1不是質數
    i = 2 # 從2開始檢查
    while True:
        if i > n: break # 若已檢查完所有數字，則跳出
        if not p[i]: # 若i不是質數，則跳過
            i += 1
            continue
        if is_prime(i, prime): # 若i是質數
            prime.append(i) # 將i加入已找到的質數列表
            for j in range(i*2, n+1, i): # 將i的倍數標記為非質數
                p[j] = False
        i += 1
    return prime
    

# 測試執行時間
import timeit

def test():
    find_primes(100000)

# 重複執行 5 次，每次執行函式 1000 次，取平均時間
time_taken = timeit.timeit(test, number=1000)
print(f"平均每次執行花費：{time_taken / 1000:.8f} 秒")