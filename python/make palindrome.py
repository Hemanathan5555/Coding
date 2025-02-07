a="acbca"
temp=a
count=0
for i in range(0,len(a)-2):
    a=a[:i]+a[i+1:]
    if a==a[::-1]:
        count+=1 
    else:
        a=temp
if count==1:
    print(a)
else:
    pass
