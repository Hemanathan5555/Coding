a=[203,204,205,206,207,208,203,204,205,206]
b=[203,204,204,205,206,207,205,208,203,206,205,206,204]
s=set(a)#change into set to remove duplicate
for i in s:
    if a.count(i)!=b.count(i):#if the occurance of i in a not equal to occurance of i in b
        print(i)
    else:
        pass
