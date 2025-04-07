a, n = map(int, input().split())

if a == 0:
    print(0)
    exit()
elif n < 2 or n > 36:
    print('只支援2~36進制的轉換!')
    exit()

is_negative = a < 0
a = abs(a)

# 計算最高次冪
e = 0
while n ** e <= a:
    e += 1
e -= 1  # 找到適合的最大次冪

if is_negative:
    print('-', end='')

for i in range(e, -1, -1):
    num = n ** i
    digit = a // num
    a %= num

    # 以下是為了處理n>10時可能會出現digit>=10而需要用字母表示的情況
    # 若 digit >= 10，轉換成字母
    if digit >= 10:
        print(chr(ord('A') + (digit - 10)), end='')
    else:
        print(digit, end='')


'''我的
a, n = map(int, input().split())

if a == 0:
    print(0)
else:
    if a < 0:
        print('-', end='')

    e = int(math.log(a, n))

    for i in range(e, -1, -1):
        num = n ** i
        #print('i =', i)
        #print('num =', num)
        print(a // num, end='')
        a %= num
'''