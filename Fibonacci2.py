n = [1,1]
#print("1, 1, ", end = "")
for i in range(2,200):
    n.append(n[i-1] + n[i-2])
    #print(n[i], end = ", ")
    print(f"第{i-1}項除以第{i-2}項的商為{n[i-1]/n[i-2]}")
    