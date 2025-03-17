a = [3, 1, 4]  
b = [8, 2, 6]
a.sort()
b.sort()
count=0
for i in range(0,len(a)):
    c=a[i]*b[i]
    count=count+c
print(count)
