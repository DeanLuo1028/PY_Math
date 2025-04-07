def gcd(a, b): # 計算最大公因數
    if a == 0: return b
    if b == 0: return a
    while b:
        a, b = b, a % b
    return a

def lcm(a, b): # 計算最小公倍數
    return a * b // gcd(a, b)

# Fractions類別是分數
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
        if self.eq0(): return "0"
        return str(self.n) + "/" + str(self.d)
    
    def copy(self): # 複製分數
        return Fraction(self.n, self.d)

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

    def eq0(self):
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
        elif isinstance(other, Decimal): return self.add(other.convert_to_fraction())
        self.find_common_denominator(other)
        self.n += other.n # 分子相加
        self.simplify() # 約分成最簡分數
        return self
    
    def __add__(self, other): # 加法
        if type(other)==int:
            return self.__add__(Fraction(other, 1))
        elif isinstance(other, Decimal): return self - other.convert_to_fraction()
        self.find_common_denominator(other)
        f = Fraction(self.n + other.n, self.d) # 新分數
        f.simplify() # 約分成最簡分數
        self.simplify() # 約分成最簡分數
        other.simplify() # 約分成最簡分數
        return f
    
    def subtract(self, other): # 減
        if type(other)==int:
            return self.subtract(Fraction(other, 1))
        elif isinstance(other, Decimal): return self.subtract(other.convert_to_fraction())
        self.find_common_denominator(other)
        self.n -= other.n # 分子相減
        self.simplify() # 約分成最簡分數
        return self

    def __sub__(self, other): # 減法
        if type(other)==int:
            return self.__sub__(Fraction(other, 1))
        elif isinstance(other, Decimal): return self - other.convert_to_fraction()
        self.find_common_denominator(other)
        f = Fraction(self.n - other.n, self.d) # 新分數
        f.simplify() # 約分成最簡分數
        self.simplify() # 約分成最簡分數
        other.simplify() # 約分成最簡分數
        return f
    
    def multiply(self, other): # 乘
        if type(other)==int:
            return self.multiply(Fraction(other, 1))
        elif isinstance(other, Decimal): return self.multiply(other.convert_to_fraction())
        self.n *= other.n # 分子相乘
        self.d *= other.d # 分母相乘
        self.simplify() # 約分成最簡分數
        return self

    def __mul__(self, other): # 乘法
        if type(other)==int:
            return self.__mul__(Fraction(other, 1))
        elif isinstance(other, Decimal): return self * other.convert_to_fraction()
        f = Fraction(self.n * other.n, self.d * other.d) # 新分數
        f.simplify() # 約分成最簡分數
        return f
    
    def divide(self, other): # 除
        if type(other)==int:
            if other == 0: raise ValueError("不能除以零！")
            return self.divide(Fraction(other, 1))
        elif isinstance(other, Decimal): return self.divide(other.convert_to_fraction())
        if other.eq0(): raise ValueError("不能除以零！")
        # 除法就是乘上除數的倒數
        self.n *= other.d
        self.d *= other.n
        self.simplify() # 約分成最簡分數
        return self

    def __truediv__(self, other): # 除法
        if type(other)==int:
            if other == 0: raise ValueError("不能除以零！")
            return self.__truediv__(Fraction(other, 1))
        elif isinstance(other, Decimal): return self / other.convert_to_fraction()
        if other.eq0(): raise ValueError("不能除以零！")
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
        return a.__add__(b)
    
    @staticmethod
    def subtraction(a1,a2,b1,b2): # 靜態方法，用於減法
        a = Fraction(a1, a2)
        b = Fraction(b1, b2)
        return a.__sub__(b)
    
    @staticmethod
    def multiplication(a1,a2,b1,b2): # 靜態方法，用於乘法
        a = Fraction(a1, a2)
        b = Fraction(b1, b2)
        return a.__mul__(b)
    
    @staticmethod
    def division(a1,a2,b1,b2): # 靜態方法，用於除法
        a = Fraction(a1, a2)
        b = Fraction(b1, b2)
        return a.__truediv__(b)
    
    def convert_to_decimal(self): # 轉換成Decimal
        return Decimal(str(self.n)) / Decimal(str(self.d)) # 分子分母都轉成Decimal再相除
    

# Decimal類別是小數
# 特點是用字串表示小數，並提供各種數學運算功能
class Decimal:
    def __init__(self, s): # 特點是用字串表示小數
        s = s.strip()  # 移除空白字元
        self.is_positive = False if s[0] == '-' else True  # 負數處理
        s = s.lstrip('-')  # 移除負號
        l = s.split('.') # 將字串分割成整數部分和小數部分
        self.i = int(l[0])  # 整數部分
        self.d = l[1] if len(l) > 1 else '0'  # 小數部分
    # 轉回字串
    def __str__(self):
        self.remove0()
        return str(self.i) + '.' + self.d if self.is_positive else '-' + str(self.i) + '.' + self.d
    # 轉回浮點數
    def __float__(self):
        self.remove0()
        return float(str(self.i) + '.' + self.d) if self.is_positive else -float(str(self.i) + '.' + self.d)
    # 轉回整數
    def __int__(self): return self.i if self.is_positive else -self.i
    # 重複印出
    def __repr__(self): return str(self)
    # 輸出值
    def value(self): return float(self)
    # 複製
    def copy(self): return Decimal(str(self))
    # 在末尾添加n個0
    def add0(self, n):
        self.d += '0' * n
        return self
    # 移除末尾的0
    def remove0(self):
        self.d = self.d.rstrip('0')
        if self.d == '': self.d = '0'  # 若小數部分全為0，則設為0，這樣設計是為了知道這是一個小數而不是整數
        return self
    # 絕對值
    def abs(self):
        n = self.copy()
        n.is_positive = True
        return n
    # 相反數
    def opposite(self):
        n = self.copy()
        n.is_positive = not n.is_positive
        return n
    # 判斷是否為0
    def eq0(self): 
        self.remove0()
        return str(self) == '0.0'
    # 判斷兩數是否相等，可以是整數、浮點數、Decimal
    def __eq__(self, other):
        if isinstance(other, int): return self.__eq__(Decimal(str(other)))
        if isinstance(other, float): return float(self) == other
        if isinstance(other, Decimal):
            self.remove0()
            other.remove0()
            if self.is_positive == other.is_positive:  # 正負相同才比較
                return self.i == other.i and self.d == other.d
            else: return False
        return False
    # 判斷兩數是否不等
    def __ne__(self, other): return not self.__eq__(other)
    # 判斷兩數是否小於
    def __lt__(self, other):  # 小於
        if isinstance(other, int): return self.__lt__(Decimal(str(other)))
        if isinstance(other, float): return float(self) < other
        if isinstance(other, Decimal):
            self.remove0()
            other.remove0()
            if self.is_positive and other.is_positive:  # 都為正才比較
                return self.i < other.i or (self.i == other.i and self.d < other.d)
            elif not self.is_positive and not other.is_positive:  # 都為負才比較
                return self.i > other.i or (self.i == other.i and self.d > other.d)
            elif self.is_positive and not other.is_positive:  # 正負不同，正的大
                return False
            else:  # 正負不同，負的大
                return True
        return False
    # 判斷兩數是否大於
    def __gt__(self, other): return not self.__lt__(other) and self.__ne__(other)
    # 判斷兩數是否小於等於
    def __le__(self, other): return not self.__gt__(other)
    # 判斷兩數是否大於等於
    def __ge__(self, other): return not self.__lt__(other)
    # 加法，可以是整數、浮點數、Decimal
    def __add__(self, other):
        if isinstance(other, int): return Decimal(str(self.i + other) + '.' + self.d)
        elif isinstance(other, float): return self + Decimal(str(other))
        elif isinstance(other, Fraction): return self + other.convert_to_decimal()
        # 小數相加
        if self.eq0() or other.eq0(): return other if self.eq0() else self  # 只要有一個是0，就返回另一個
        elif self.is_positive and not other.is_positive: # 正加負
            return self - other.abs()
        elif not self.is_positive and other.is_positive: # 負加正
            return other - self.abs()
        else: # 兩數皆為正或皆為負
            # 創建複製，不改變原物件
            self_copy = self.copy()
            other_copy = other.copy()
            
            # 將小數部分補足到相同長度
            if len(self_copy.d) < len(other_copy.d):
                self_copy.add0(len(other_copy.d) - len(self_copy.d))
            elif len(self_copy.d) > len(other_copy.d):
                other_copy.add0(len(self_copy.d) - len(other_copy.d))
            # 計算新的整數和小數部分
            s = int(str(self_copy.i) + self_copy.d)
            o = int(str(other_copy.i) + other_copy.d)
            total = s + o
            # 將結果轉回字串，並重建 Decimal
            total_str = str(total)
            d_len = len(self_copy.d)
            # 檢查整數和小數部分，避免空字串錯誤
            int_part = total_str[:-d_len] if len(total_str) > d_len else '0'
            dec_part = total_str[-d_len:] if d_len > 0 else '0'
            # 重建 Decimal 物件並返回結果
            result = Decimal(int_part + '.' + dec_part)
            result.is_positive = self.is_positive # 正負相同
            return result.remove0()

    def __sub__(self, other):
        if isinstance(other, int): return self - Decimal(str(other))
        elif isinstance(other, float): return self - Decimal(str(other))
        elif isinstance(other, Fraction): return self - other.convert_to_decimal()
        if self == other: return Decimal('0')
        elif other.eq0(): return self # 任何數減0都會是原數
        elif self.eq0(): return other.opposite()  # 0減正數為負數, 0減負數為正數
        elif self > other:  # 大減小為正
            self_copy = self.copy()
            other_copy = other.copy()
        
            # 將小數部分補足到相同長度
            if len(self_copy.d) < len(other_copy.d):
                self_copy.add0(len(other_copy.d) - len(self_copy.d))
            elif len(self_copy.d) > len(other_copy.d):
                other_copy.add0(len(self_copy.d) - len(other_copy.d))
        
            # 將整數和小數部分轉為相同精度的整數再相減
            s = int(str(self_copy.i) + self_copy.d)
            o = int(str(other_copy.i) + other_copy.d)
            total = s - o

            # 構建結果字符串
            total_str = str(total)
            d_len = len(self_copy.d)  # 保持原始小數位數
            int_part = total_str[:-d_len] if len(total_str) > d_len else '0'
            dec_part = total_str[-d_len:].rjust(d_len, '0')  # 確保小數部分長度一致

            # 重建 Decimal 物件並返回結果
            result = Decimal(int_part + '.' + dec_part)
            result.is_positive = self.is_positive  # 保持正負號
            result.remove0()
            return result
        else:  # 小減大為負
            result = other - self
            result = result.opposite()  # 變負數
            return result

    def __mul__(self, other):
        if isinstance(other, int):
            return Decimal(str(self.i * other) + '.' + self.d)
        elif isinstance(other, Fraction): return self * other.convert_to_decimal()
        if self.eq0() or other.eq0(): return Decimal('0') # 只要有一個是0，就返回0
        # 計算乘積
        s = int(str(self.i) + self.d)
        o = int(str(other.i) + other.d)
        total = s * o

        # 將結果轉回字串，並重建 Decimal
        total_str = str(total)
        d_len = len(self.d) + len(other.d)  # 乘積後的小數位數
        int_part = total_str[:-d_len] if len(total_str) > d_len else '0'
        dec_part = total_str[-d_len:].rjust(d_len, '0')  # 確保小數部分長度一致

        # 重建 Decimal 物件並返回結果
        result = Decimal(int_part + '.' + dec_part)
        result.is_positive = (self.is_positive == other.is_positive)  # 正負號相乘，相同為正，不同為負
        result.remove0()
        return result
    
    def __truediv__(self, other):
        if isinstance(other, int):
            return self / Decimal(str(other))
        elif isinstance(other, Fraction): return self / other.convert_to_decimal()
        if other.eq0():
            raise ZeroDivisionError('不可以除以0')
        if self.eq0(): # 0除以任何數都會是0
            return Decimal('0')
    
        # 計算商並轉成字串格式
        s = int(str(self.i) + self.d)
        o = int(str(other.i) + other.d)
        total = s / o

        # 轉成字串，分割整數和小數部分
        total_str = f"{total:.10f}".rstrip('0')  # 保持10位小數精度，並去掉末尾多餘的0
        int_part, dec_part = total_str.split('.') if '.' in total_str else (total_str, '0')

        # 重建 Decimal 物件並返回結果
        result = Decimal(int_part + '.' + dec_part)
        result.is_positive = (self.is_positive == other.is_positive)  # 正負號相除，相同為正，不同為負
        return result.remove0()
    
    def __floordiv__(self, other): 
        result = self / other
        return result.i if result > 0 else -(result.i + 1) # 
    
    # 四捨五入
    def round(self, n):
        if self.eq0(): return self  # 0 不用四捨五入
        self.remove0()  # 先移除末尾多餘的0
        if n == 0:
            # 四捨五入到整數
            if int(self.d[0]) >= 5:
                return Decimal(str(int(self) + 1))
            else:
                return Decimal(str(int(self)))
        else:
            # 小數部分四捨五入到第 n 位
            if len(self.d) <= n:
                # 如果小數部分長度不超過 n，無需四捨五入
                return self.copy()
            
            # 判斷第 n+1 位數字是否 >= 5
            if int(self.d[n]) >= 5:
                # 進位處理
                integer_part = str(self.i)
                decimal_part = self.d[:n]  # 取得四捨五入之前的前 n 位
                round_value = int(decimal_part) + 1  # 進位
                
                # 如果進位導致小數部分長度超過 n 位，需要處理進位至整數部分
                if len(str(round_value)) > n:
                    integer_part = str(int(integer_part) + 1)
                    decimal_part = '0' * n
                else:
                    decimal_part = str(round_value).zfill(n)  # 填充0以保證小數位數的長度
            else:
                # 無需進位，直接取前 n 位
                integer_part = str(self.i)
                decimal_part = self.d[:n]
            
            # 組合成新的 Decimal
            return Decimal(integer_part + '.' + decimal_part).remove0()


    def convert_to_fraction(self):
        if self.eq0(): return Fraction(0, 1)
        if self.d == '0': return Fraction(self.i, 1)
        else: return Fraction(int(str(self.i) + self.d), 10**len(self.d))

if __name__ == '__main__':
    a = Decimal('0.5')
    b = Fraction(1, 2)
    c = a - b
    print(type(c))
    print(c)
    print(c.eq0())
    d = b - a
    print(type(d))
    print(d)
    print(d.eq0())