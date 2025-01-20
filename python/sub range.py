a=[2, 3, 1, 2, 3, 2, 3, 3]
k=[[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
res = []
for i in k:
    l=[]
    for j in range(i[0],i[1]):
        l.append(a[j])
    res.append(l)
print(res)
   
   
   
    
