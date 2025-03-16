a=[-3, 2, -1, 5, 4]
count=0
for i in a:
    if i<0:
        i=i+(i*-2)
        count=count+i
    else:
        count=count+i
print(count)
