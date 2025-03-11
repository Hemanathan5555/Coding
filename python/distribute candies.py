a=[2,4,3,5,2,6,4,5]
count=0
sums=len(a)*1
for i in range(0,len(a)-1):
    if a[i]<a[i+1]:
        count=count+1
        sums=sums+count
    else:
        count=0
        sums=sums+count
print(sums)
