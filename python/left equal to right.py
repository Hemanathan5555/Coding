a=[1,1,4,1,1]
count=0
count1=0
s=len(a)//2
for i in range(0,s):
    count=count+a[i]
for j in range(s+1,len(a)):
    count1=count1+a[j]
print(count)
print(count1)
if count==count1:
    print("yes")
else:
    print("no")
