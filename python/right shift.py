b=[2,4,6,8,3]
k=b[-1]
s=len(b)-2
while b[s]>k:
    b[s+1]=b[s]
    print(b)
    s=s-1
b[s+1]=k
print(b)
    
