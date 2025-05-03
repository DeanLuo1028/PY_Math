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
    if n == 1:
        return "1 不是質數也不是合數！"

    original_n = n  # 儲存原始數字（用來最後輸出用）

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

        # 如果目前這個質數可以整除 n，就記錄次方並除以它
        if n % primes[i] == 0:
            power[i] += 1        # 次方數 +1
            n //= primes[i]      # 除以這個質數
        else:
            i += 1  # 換下一個質數

    # 以下是格式化輸出
    result = str(original_n) + " 的質因數分解為："
    first = True  # 控制是否需要加乘號

    for i in range(len(primes)):
        if power[i] != 0:  # 有出現過的質因數才顯示
            if not first:
                result += " × "  # 不是第一項就加乘號
            else:
                first = False  # 第一項以後都要加乘號
            result += str(primes[i])  # 顯示質因數
            if power[i] > 1:
                result += "^" + str(power[i])  # 顯示次方（如果次方大於 1）

    # 額外處理：如果原本是質數，則沒有乘號與次方
    if not "×" in result and not "^" in result:
        result = str(original_n) + "本來就是質數！"

    return result

# 主程式入口
if __name__ == "__main__":
    x = int(input("請輸入你要分解的數字: "))
    print(prime_factorization(x))
