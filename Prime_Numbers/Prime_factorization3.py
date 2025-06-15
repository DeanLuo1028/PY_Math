# 動態生成版
# 判斷一個數 n 是否為質數，並且只用現有的質數來測試
def is_prime(n, primes):
    if n < 2: return False
    if n == 2 or n == 3: return True  # 2 和 3 是最小的質數

    # 嘗試用已知質數 primes 中的每一個質數來除 n
    for prime in primes:
        if prime > int(n ** 0.5) + 1:  # 只需檢查到 √n 即可
            return True  # 若都沒整除，代表 n 是質數
        if n % prime == 0:  # 如果能整除，n 就不是質數

            return False

    return True  # 若走完整個迴圈都沒整除，代表 n 是質數

# 主函式：質因數分解
def prime_factorization(n):
    if n < 1: raise "請輸入正整數！"
    if n == 1:
        return [(1,1)]

    # 初始的質數列表，從 2 跟 3 開始
    primes = [2, 3]
    # 對應每個質數的次方數（初始為 0）
    power = [0, 0]

    i = 0  # 用來追蹤目前使用哪一個質數
    while n != 1:  # 當還沒分解完（n 不等於 1）
        if i >= len(primes):  # 如果已知的質數都用完了，還沒分解完，動態產生新的質數
            prime = primes[-1] + 2  # 從目前最大質數往後找下一個質數（跳過偶數）
            while not is_prime(prime, primes):  # 直到找到質數為止
                prime += 2  # 每次加 2 繼續找（跳過偶數）
            primes.append(prime)  # 加入新找到的質數
            power.append(0)       # 同時給這個質數對應一個次方數 0

        # 如果目前這個質數可以整除 n，就一直除到不能整除為止
        while n % primes[i] == 0:
            n //= primes[i]      # 除以這個質數
            power[i] += 1        # 次方數 +1
        
        i += 1  # 換下一個質數

    # 結果列表中以元組的形式存儲
    result = [(primes[i], power[i]) for i in range(len(primes)) if power[i] != 0]  # 生成結果列表
    '''上面那行等價於:
    result = []
    for i in range(len(primes)):
        if power[i] != 0:  # 有出現過的質因數才存入
            result.append((primes[i], power[i]))  # 以元組的形式存儲結果
    '''
  
    return result

# 主程式入口
if __name__ == "__main__":
    x = int(input("請輸入你要分解的數字: "))
    result = prime_factorization(x)
    print("分解結果:", x, "=", end=" ")
    for i in range(len(result)):
        print(result[i][0], "^", result[i][1], end=" ")
        if i != len(result) - 1:
            print("×", end=" ")
