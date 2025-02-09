import math as math
a=25
b=49
count=0
for i in range(a,b+1):
    c=math.sqrt(i)
    if i%c==0:
        count=count+1
    else:
        pass
print(count)
