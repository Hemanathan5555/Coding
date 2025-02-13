a=[1,7,0,8,0,9]
for i in  range(0,len(a)-2):
    for j in range(i+1,len(a)):
        if a[i]==0 and a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
            print(a)
        else:
            pass
