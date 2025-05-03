# 預先處理版
def find_primes(n): # 直接使用eratosthenes篩法
    is_prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(2, n + 1) if is_prime[x]]


def prime_factorization(x):
    if x == 1: return "1 不是質數也不是合數！"
    
    result = ""
    # 開始執行並填充primes
    primes = find_primes(int(x ** 0.5) + 1) # 只填充到 x 的平方根
    
    # 格式化輸出結果
    result = str(x) + " 的質因數分解為："
    original_x = x  # 儲存原始數字
    e = 0 # exponent 表示次方數

    for i in range(len(primes)):
        e = 0
        while x % primes[i] == 0: # 一直除直到不能再除以計算次方數
            e += 1
            x //= primes[i]  # 使用整數除法避免浮點數問題
        if e != 0:  # 如果次方不是零
            result += str(primes[i])
            if e != 1:  # 如果次方不是1，顯示次方
                result += "^" + str(e)
            if x != 1:  # 還沒分解完，顯示乘號
                result += " × "

        if x == 1:  # 分解完畢
            break
    
    # 如果result的最後一個字 是 一開始" 的質因數分解為："中最後的冒號，代表x沒有任何質因數
    if result[-1] == "：":
        result = str(original_x) + "本來就是質數！"
    
    return result

if __name__ == "__main__":
    x = int(input("請輸入你要分解的數字: "))
    print(prime_factorization(x))
