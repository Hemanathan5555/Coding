a=[1,1,2,3,3]
s=set(a)
count=0
for i in s:
    k=a.count(i)
    if k>1:
        count=count+1
    else:
        pass
print(count)
