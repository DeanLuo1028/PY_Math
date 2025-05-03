def is_prime(x):
    if x <= 1: return False
    if x == 2: return True
    # 只檢查比 n 的平方根小的質數
    sqrt = int(x ** 0.5) + 1
    for n in range(2,sqrt+1): 
        if x % n == 0:
            return False 
            
    return True

for i in range(1001):
    if is_prime(i):
        print(i,sep="", end=", ")