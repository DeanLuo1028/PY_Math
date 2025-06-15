'''
def sigma(a, b, f):
    if a > b: a, b = b, a
    return sum(map(f, range(a, b+1)))
'''
def sigma(a: int, b: int, f: function) -> int: ...