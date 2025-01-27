a=20
m=3
k=6
d=85
count=0
n=6
c=0
while a>0:
    count=count+a#creating a variable and adding a
    a=a-m
    c=c+1
    if a<k:#if a becomes less than k the loop breaks
     break

while count>0:
    count=count+k#adding k with count it will be sum
    c=c+1
    if count>d:#if count became greater than 85 it breaks
        break
print(c)
