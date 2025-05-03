def is_prime(x):
    if x <= 1: return False
    if x == 2: return True
    # 只檢查比 n 的平方根小的質數
    sqrt = int(x ** 0.5) + 1
    nums = list(range(2,sqrt+1))
    for n in range(2,sqrt+1): 
        # 不在nums裡的n就是被刪掉的，不用考慮
        if not (n in nums): continue
        # 從nums中取用n，但你在迴圈裡對nums進行操作會有問題的！
        #print("n :",n)
        if x % n == 0:
            return False 
        else: # n無法整除x
            # 刪除 nums 中 n與n的倍數
            # 因為既然n無法整除x，n的倍數也不可能整除x
            # 把它們刪了可以減少計算量
            for i in range(n, sqrt+1, n):
                if i in nums: nums.remove(i)
            
    return True


for i in range(1001):
    if is_prime(i):
        print(i,sep="", end=", ")