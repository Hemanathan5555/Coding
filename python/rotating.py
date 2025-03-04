a=3
b=7
c=3
count=1
while a<b:
    a=a-1
    count=count+1
    if a==1:
        a=c
    if count==b:
        print(a)
        break
    else:
        pass
