import time
def collatz_list(n):
    l = [n]
    while n!= 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def collatz(n):
    count = 0
    while n!= 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

i = pow(10,40)
while True:
    print(i, ": ", collatz(i))
    i += 1
    time.sleep(0.1)
    #print(i, ": ", end="")
    #for j in collatz_list(i):
    #    print(j, end=", ")
    #print()