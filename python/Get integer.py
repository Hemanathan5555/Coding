n=2
k=n-1
p=7
for i in range(0,19):
    if n<p:
        k=k+1
        if k>7:
            k=0
            k=k+1
        else:
            pass
print(k)
