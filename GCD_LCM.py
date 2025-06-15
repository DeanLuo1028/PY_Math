def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
def gcd(a, b):
    if a == b: return a
    while a: # 當a不為0時才執行，a為0時，b就是最大公因數
        if a < b: a, b = b, a # a 要比較大
        a = a % b # 不斷用小的(b)去減掉大的(a)，直到a比b小，上面那行會把兩數交換
    return b
'''
def lcm(a, b): 
    if a == b: return a
    return a * b // gcd(a, b)
'''
def lcm(a, b):
    if a == b: return a
    origin_a, origin_b = a, b
    while not a == b:
        if a < b:
            a += origin_a # a一直加自己直到a=b或a>b
        elif a > b:
            b += origin_b # b一直加自己直到b=a或b>a
    return a
'''

a, b = map(int, input().split())
print("gcd(a, b) =", gcd(a, b))
print("lcm(a, b) =", lcm(a, b))