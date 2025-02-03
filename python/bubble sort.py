a=[15,28,89,8,1,78,5,34]
for j in range(0,len(a)-1):
    for i in range(0,len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(a)
