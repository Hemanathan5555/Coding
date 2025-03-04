a=[9,9,9,9,9,9,9]
b=[9,9,9,9]
c=[]
for i in range(0,len(a)):
    if len(b)<len(a):
        b.append(0)
        if len(b)==len(a):
            break
for i in range(0,len(a)):
    m=a[i]+b[i]
    c.append(m)
print(c)
    
