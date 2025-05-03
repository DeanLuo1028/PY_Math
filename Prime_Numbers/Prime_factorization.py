def is_prime(n, primes):
    if n==2 or n==3:
        return True
    # 只檢查比 n 的平方根小的質數
    sqrt = int(n ** 0.5) + 1
    for prime in primes:
        if prime > sqrt:
            return True
        if n % prime == 0:
            return False
    return True

def find_primes(limit):
    primes = [2]
    for n in range(3, limit, 2):  # 只檢查奇數
        if is_prime(n, primes):
            primes.append(n)
    return primes

def p(str): # 輸出字串且不換行
    print(str, end='')

def main():
    x = 0
    while x < 1 or x >= 100000:  # 輸入正整數
        x = int(input('你想要分解哪一個數?: '))
        if x < 1 or x >= 100000:
            print('輸入錯誤，請輸入1到100000之間的正整數')
        else:
            if x == 1:
                p('1 不是質數也不是合數！')
                return # 結束程式
            break
    
    # 開始執行並填充primes
    primes = find_primes(x)
    
    if x in primes:  # 如果x 在primes裡面，表示 x 是質數，直接顯示
        p(f'{x} 本來就是質數！')
        return # 結束程式
    
    e = 0
    p(f'分解的結果是 {x} = ')

    for i in range(len(primes)):
        e = 0
        while x % primes[i] == 0:
            e += 1
            x //= primes[i]  # 使用整數除法避免浮點數問題
        if e != 0:  # 如果次方不是零
            p(f'{primes[i]}')
            if e != 1:  # 如果次方不是1，顯示次方
                p(f'^{e}')
            if x != 1:  # 還沒分解完，顯示乘號
                p(' × ')

        if x == 1:  # 分解完畢
            break

if __name__ == '__main__':
    main()
