def gcd(a, b): # 計算最大公因數
    if a == 0: return b
    if b == 0: return a
    while b:
        a, b = b, a % b
    return a

def lcm(a, b): # 計算最小公倍數
    return a * b // gcd(a, b)

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("分母不能為零！")
        self.n = numerator # numerator 是分子
        self.d = denominator # denominator 是分母
        self.simplify() # 約分成最簡分數

    def value(self): # 輸出分數的值
        return self.n / self.d
    
    def value_int(self): # 輸出分數的值(整數)
        return int(self.value())
    
    def __repr__(self): # 輸出分數的字串表示
        return "Fraction(" + str(self.n) + ", " + str(self.d) + ")"
    
    def __str__(self): # 輸出分數的字串表示
        if self.is0(): return "0"
        return str(self.n) + "/" + str(self.d)
    
    def __eq__(self, other):
        if isinstance(other, Fraction): # 判斷other是不是Fraction類的
            self.simplify()
            other.simplify()
            return self.n == other.n and self.d == other.d
        return False
    
    def is_greater(self, other):
        if isinstance(other, Fraction): # 判斷other是不是Fraction類的
            if self == other: return False
            self.simplify()
            other.simplify()
            self.find_common_denominator(other)
            return self.n > other.n
        return False
    
    def is_less(self, other):
        if isinstance(other, Fraction): # 判斷other是不是Fraction類的
            if self == other: return False
            self.simplify()
            other.simplify()
            self.find_common_denominator(other)
            return self.n < other.n
        return False

    def is0(self):
        if self.n == 0:
            self.d = 1
            return True
        return False    
    
    def expand(self, x): # 擴分
        self.n *= x
        self.d *= x
        return
    
    def simplify(self): # 約分成最簡分數
        g = gcd(self.n, self.d)
        self.n //= g
        self.d //= g
        return
    
    def find_common_denominator(self, other): # 通分
        l = lcm(self.d, other.d) # 最小公倍數
        self.expand(l // self.d) # 分子分母同乘(l除以分母)以擴分
        other.expand(l // other.d) # # 分子分母同乘(l除以分母)以擴分
        return
    
    def add(self, other): # 加
        if type(other)==int:
            return self.add(Fraction(other, 1))
        self.find_common_denominator(other)
        self.n += other.n # 分子相加
        self.simplify() # 約分成最簡分數
        return self
    
    def add_value(self, other): # 加法
        if type(other)==int:
            return self.add_value(Fraction(other, 1))
        self.find_common_denominator(other)
        f = Fraction(self.n + other.n, self.d) # 新分數
        f.simplify() # 約分成最簡分數
        self.simplify() # 約分成最簡分數
        other.simplify() # 約分成最簡分數
        return f
    
    def subtract(self, other): # 減
        if type(other)==int:
            return self.subtract(Fraction(other, 1))
        self.find_common_denominator(other)
        self.n -= other.n # 分子相減
        self.simplify() # 約分成最簡分數
        return self

    def subtract_value(self, other): # 減法
        if type(other)==int:
            return self.subtract_value(Fraction(other, 1))
        self.find_common_denominator(other)
        f = Fraction(self.n - other.n, self.d) # 新分數
        f.simplify() # 約分成最簡分數
        self.simplify() # 約分成最簡分數
        other.simplify() # 約分成最簡分數
        return f
    
    def multiply(self, other): # 乘
        if type(other)==int:
            return self.multiply(Fraction(other, 1))
        self.n *= other.n # 分子相乘
        self.d *= other.d # 分母相乘
        self.simplify() # 約分成最簡分數
        return self

    def multiply_value(self, other): # 乘法
        if type(other)==int:
            return self.multiply_value(Fraction(other, 1))
        f = Fraction(self.n * other.n, self.d * other.d) # 新分數
        f.simplify() # 約分成最簡分數
        self.simplify() # 約分成最簡分數
        other.simplify() # 約分成最簡分數
        return f
    
    def divide(self, other): # 除
        if type(other)==int:
            if other == 0: raise ValueError("不能除以零！")
            return self.divide(Fraction(other, 1))
        if other.is0(): raise ValueError("不能除以零！")
        # 除法就是乘上除數的倒數
        self.n *= other.d
        self.d *= other.n
        self.simplify() # 約分成最簡分數
        return self

    def divide_value(self, other): # 除法
        if type(other)==int:
            if other == 0: raise ValueError("不能除以零！")
            return self.divide_value(Fraction(other, 1))
        if other.is0(): raise ValueError("不能除以零！")
        # 除法就是乘上除數的倒數
        f = Fraction(self.n * other.d, self.d * other.n) # 新分數
        f.simplify() # 約分成最簡分數
        self.simplify() # 約分成最簡分數
        other.simplify() # 約分成最簡分數
        return f
    
    @staticmethod
    def addition(a1,a2,b1,b2): # 靜態方法，用於加法
        a = Fraction(a1, a2)
        b = Fraction(b1, b2)
        return a.add_value(b)
    
    @staticmethod
    def subtraction(a1,a2,b1,b2): # 靜態方法，用於減法
        a = Fraction(a1, a2)
        b = Fraction(b1, b2)
        return a.subtract_value(b)
    
    @staticmethod
    def multiplication(a1,a2,b1,b2): # 靜態方法，用於乘法
        a = Fraction(a1, a2)
        b = Fraction(b1, b2)
        return a.multiply_value(b)
    
    @staticmethod
    def division(a1,a2,b1,b2): # 靜態方法，用於除法
        a = Fraction(a1, a2)
        b = Fraction(b1, b2)
        return a.divide_value(b)
    
    
if __name__ == "__main__":
    a = Fraction(1, 4) # 1/4
    b = Fraction(2, 4) # 1/2
    print('a =',a)
    print('b =',b)
    print(a.is_greater(b)) # False
    print(a.is_less(b)) # True
    
    

"""
    @staticmethod
    def print_fraction(a): # 靜態方法，用於輸出分數
        a.print()
        return"""    
"""
    def add(self, other): # 加
        f_self, f_other = self.find_common_denominator(other)
        self.n = f_self.n + f_other.n # 分子相加
        self.d = f_self.d
        self.simplify() # 約分成最簡分數
        return self
    
    def add_value(self, other): # 加法
        f_self, f_other = self.find_common_denominator(other)
        f = Fraction(f_self.n + f_other.n, f_self.d) # 新分數
        f.simplify() # 約分成最簡分數
        return f
    
    def subtract(self, other): # 減
        f_self, f_other = self.find_common_denominator(other)
        self.n = f_self.n - f_other.n # 分子相減
        self.d = f_self.d
        self.simplify() # 約分成最簡分數
        return self

    def subtract_value(self, other): # 減法
        f_self, f_other = self.find_common_denominator(other)
        f = Fraction(f_self.n - f_other.n, f_self.d) # 新分數
        f.simplify() # 約分成最簡分數
        return f
    
    def multiply(self, other): # 乘
        self.n *= other.n # 分子相乘
        self.d *= other.d # 分母相乘
        self.simplify() # 約分成最簡分數
        return self

    def multiply_value(self, other): # 乘法
        f = Fraction(self.n * other.n, self.d * other.d) # 新分數
        f.simplify() # 約分成最簡分數
        return f
    
    def divide(self, other): # 除
        self.n *= other.d
        self.d *= other.n
        self.simplify() # 約分成最簡分數
        return self
    
    
    @staticmethod
    def find_common_denominator(self, other): # 通分
        l = lcm(self.d, other.d) # 最小公倍數
        return Fraction(self.n * (l // self.d), l), Fraction(other.n * (l // other.d), l)
    """
    