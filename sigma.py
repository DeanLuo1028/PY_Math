def sigma(a, b, f):
    if a > b: a, b = b, a
    return sum(map(f, range(a, b+1)))
    #return sum(f(i) for i in range(a, b+1))