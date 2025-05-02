import math

def is_prime(n):
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

if __name__ == "__main__":
    num = 1000000000000
    pn = 0
    maxGap = 0
    
    while True:
        if is_prime(num):
            pn += 1
            print(f"{num}是第{pn}個質數",end=",")
            if pn == 1:
                previousNum = num
            else:
                if num - previousNum > maxGap:
                    maxGap = num - previousNum
                print(f"它跟前一個質數相差{num - previousNum}")
                previousNum = num

        num+=1
        if num > 1000000100000:
            break

    #print(f"最多質數數量為{pn}個")
    print(f"最大質數差為{maxGap}")
