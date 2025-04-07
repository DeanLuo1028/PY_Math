n = [1,1]
for i in range(2,20):
    n.append(n[i-1] + n[i-2])
print(n)