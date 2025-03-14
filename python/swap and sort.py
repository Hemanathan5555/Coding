a=[3,1,2]
s=sorted(a)
found=False
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        a[i],a[j]=a[j],a[i]
        if a==s:
            print("yes")
            found=True
            break
        else:
            a[i],a[j]=a[j],a[i]
    if found:
        break
if not found:
    print("no")
