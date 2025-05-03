import numpy as np
from Decimal import Decimal as Dec

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

# 解聯立方程 Ax = b
x = np.linalg.solve(A, b)
print(x)  # 輸出: [ -4.   4.5]

# 計算行列式
det = Dec(np.linalg.det(A))
det = det.round(5)
print(det)  # 輸出: -2.0000000000000004

# 計算反矩陣
A_inv = np.linalg.inv(A)
print(A_inv)
