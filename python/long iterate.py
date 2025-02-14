a=3
temp=a
count=1
for i in range(0,30):
    a=a-1
    count=count+1
    if a==1:
        a=count+temp
        count=count+1
    if count==15:
        print(a)
    else:
        pass
