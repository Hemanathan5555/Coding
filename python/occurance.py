a="aaabbcc"
c=list(a)
n=0
k=1
for i in range(0,9):
    if c[n]==c[k]:
        c.remove(c[n])
        c.remove(c[k])
        n=n+2
        k=k+2
    else:
        n=n+1
        k=k+1
    if n==6:
        break
print(c)
        
