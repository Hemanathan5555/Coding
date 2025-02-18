a=[3,1,2]
b=sorted(a)
for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        a=a[i+1:]+a[:i+1]
        if a==b:
            print("yes")
        else:
            pass
        
