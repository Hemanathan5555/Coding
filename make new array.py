a=[1,2,3,4,5]
b=[]
e=[]
for i in range(0,len(a)-1):
    c=a[i+1]-a[i]
    b.append(c)
for i in range(0,len(a)-1):
    if a[i+1]-a[i]==min(b):
        e.append(a[i])
        e.append(a[i+1])
print(e)
