a=[100,90,90,80]
b=[70,80,105]
s=set(a)
print(s)
i=0
while i<len(b):
    count=1
    for j in s:
        if j>b[i]:
            count=count+1
    print(count)
    i=i+1
