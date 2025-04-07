#Recurrence relation 的意思是 遞迴關係式
n = [1]            #定義第一項
print(f"x1={n[0]}")
def f(x):   #定義遞迴式
    return x+5
    
num = 5     #項數 
for i in range (1,num):#迭代，1表示第2項
    n.append(f(n[i-1]))
    print(f"x{i+1}={n[i]}")
    
print("總和 =",sum(n))