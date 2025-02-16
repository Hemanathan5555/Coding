a=[1,7,2,4]
b=[]
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        c=a[i]+a[j]
        if c%3!=0:
            b.append(a[i])
            b.append(a[j])
        else:
            pass
print(set(b))
            
