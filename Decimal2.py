# 由於太難寫，這段程式已棄用
class Decimal:
    def __init__(self, s):
        self.is_positive = False if s[0] == '-' else True  # 負數處理
        s = s.lstrip('-')  # 移除負號
        l = s.split('.')
        self.i = int(l[0])  # 整數部分
        self.d = []
        if len(l) == 1:  # 只有整數部分
            self.d.append('0')  # 加上一個0
        else:  # 有小數部分
            list = l[1]
            for n in list:
                self.d.append(int(n))  # 將小數部分轉為整數列表

    def str_d(self):
        return ''.join(str(i) for i in self.d)
    
    def __str__(self):
        self.remove0()
        return str(self.i) + '.' + self.str_d() if self.is_positive else '-' + str(self.i) + '.' + self.str_d()

    def __float__(self):
        self.remove0()
        return float(str(self.i) + '.' + self.str_d()) if self.is_positive else -float(str(self.i) + '.' + self.str_d())

    def __int__(self):
        return self.i if self.is_positive else -self.i

    def value(self):
        return float(self)

    def add0(self, n):  # 在末尾添加n個0
        for _ in range(n): self.d.append(0)
        return self

    def remove0(self):
        # 移除末尾的0
        while self.d[-1] == 0:
            self.d.pop() # pop() 會移除列表最後一個元素
        if self.d == []: self.d.append(0)  # 若小數部分全為0，則設為0，這樣設計是為了知道這是一個小數而不是整數
        return self

    def opposite(self):
        n = Decimal(str(self))
        n.is_positive = not n.is_positive
        return n

    def __eq__(self, other):
        if isinstance(other, int): return self.__eq__(Decimal(str(other)))
        if isinstance(other, float): return float(self) == other
        if isinstance(other, Decimal):
            self.remove0()
            other.remove0()
            if self.is_positive == other.is_positive:  # 正負相同才比較
                return self.i == other.i and self.d == other.d
            else: return False

    def __ne__(self, other): return not self.__eq__(other)

    def d_lt(self, other):  # 小數部分比較
        # 創建複製，不改變原物件
        self_copy = Decimal(str(self))
        other_copy = Decimal(str(other))
        # 將小數部分補足到相同長度
        if len(self_copy.d) < len(other_copy.d):
            self_copy.add0(len(other_copy.d) - len(self_copy.d))
        elif len(self_copy.d) > len(other_copy.d):
            other_copy.add0(len(self_copy.d) - len(other_copy.d))
        # 逐位比較
        for i in range(len(self_copy.d)):
            if self_copy.d[i] > other_copy.d[i]: return False
        return True

    def __lt__(self, other):  # 小於
        if isinstance(other, int): return self.__lt__(Decimal(str(other)))
        if isinstance(other, float): return float(self) < other
        if isinstance(other, Decimal):
            if self == other: return False # 相等不會小於
            self.remove0()
            other.remove0()
            if self.is_positive and other.is_positive:  # 都為正才比較
                return self.i < other.i or (self.i == other.i and self.d_lt(other))
            elif not self.is_positive and not other.is_positive:  # 都為負才比較
                return self.i > other.i or (self.i == other.i and self.d_lt(other))
            elif self.is_positive and not other.is_positive:  # 正負不同，正的大
                return False
            else:  # 正負不同，負的大
                return True

    def __gt__(self, other): return not self.__lt__(other) and self.__ne__(other)

    def __le__(self, other): return not self.__gt__(other)

    def __ge__(self, other): return not self.__lt__(other)

    def __add__(self, other):
        if isinstance(other, int):
            return Decimal(str(self.i + other) + '.' + self.d)
        if self.is_positive == other.is_positive: pass # 正負相同才相加
        elif self.is_positive and not other.is_positive: # 正加負
            return self - other.opposite()
        else: # 負加正
            return other - self.opposite()
        # 創建複製，不改變原物件
        self_copy = Decimal(str(self))
        other_copy = Decimal(str(other))
        
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
        
        result = Decimal(int_part + '.' + dec_part)
        result.is_positive = self.is_positive # 正負相同
        return result.remove0()

    def __sub__(self, other):
        if isinstance(other, int): return self - Decimal(str(other))
        if self == other: return Decimal('0')
        elif self > other:  # 大減小為正
            self_copy = Decimal(str(self))
            other_copy = Decimal(str(other))
            
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
            d_len = len(self_copy.d)
            int_part = total_str[:-d_len] if len(total_str) > d_len else '0'
            dec_part = total_str[-d_len:] if d_len > 0 else '0'

            # 重建 Decimal 物件並返回結果
            result = Decimal(int_part + '.' + dec_part)
            result.is_positive = self.is_positive  # 保持正負號
            return result.remove0()
        else:  # 小減大為負
            result = Decimal(str(other - self))
            result = result.opposite()  # 變負數
            return result.remove0()

# 測試
a = Decimal('9.9')
b = Decimal('1.1')
c = a + b
d = a - b
print('c =', c)  # 預期輸出：c = 11.0
print('d =', d)  # 預期輸出：d = 8.8
