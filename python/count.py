a=[1,1,2,3,3]
s=set(a)#removing duplicates
count=0
for i in s:
    k=a.count(i)
    if k>1:#if count of an interger is more than 1
        count=count+1
    else:
        pass
print(count)
