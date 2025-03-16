a=[1,5,4,3,2,6]
k=sorted(a)
right,left=-1,-1
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        if left==-1:
            left=i
    right=i+1
subarr=a[left:right+1]
subarr.sort()
arr=a[:left]+s
ubarr+a[right+1:]
if arr==k:
    print("yes")
else:
    print("no")

