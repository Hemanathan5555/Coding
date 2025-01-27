a=[7,8,4,3,1,9]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:#if i>j
            a[i],a[j]=a[j],a[i]#it will get swap
        else:
            pass
print(a)
