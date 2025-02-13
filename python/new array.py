a=[1,2,3]
k=len(a)-1
for i in range(0,3):
    a=a[k:]+a[:k]
    print(a)
