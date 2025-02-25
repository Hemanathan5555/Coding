a=[1,5,3,4,2]
count=0
k=2
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i]>a[j]:
            c=a[i]-a[j]
            if c==k:
                count=count+1
            else:
                pass
        else:
            pass
print(count)
    
