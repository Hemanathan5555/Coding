a=[1,2,3,2,8,10]
maxi=0
for i in range(0,len(a)):
    if a[i]>maxi:
        maxi=a[i]
        index=i
print(index)
