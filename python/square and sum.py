a=1
for i in range(9,100):
    c=str(i*i)
    d=len(c)//2
    m=c[:d]
    k=c[d:]
    if int(m)+int(k)==i:
        print(i)
    else:
        pass
