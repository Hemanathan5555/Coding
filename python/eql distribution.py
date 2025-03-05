a="cdcdcdcdeeeef"
b=[]
s=set(a)
count=0
for i in s:
    c=a.count(i)
    b.append(c)
for i in b:
    if i%2==1:
        count=count+1
    else:
        pass
if  count<=1:
    print("yes")
else:
    print("no")
