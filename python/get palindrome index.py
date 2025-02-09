a="abda"
temp=a
count=0
for i in range(0,len(a)):
    a=a[:i]+a[i+1:]
    if a==a[::-1]:
        print(i)
        break
    else:
        a=temp
    
