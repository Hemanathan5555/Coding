a=[2,4,5,6,7,9,11,12]
k=2
n=len(a)
count=0
i=0
while i<n:
    count=count+1
    loc=a[i]+k
    while i<n and a[i]<=loc:
        i=i+1
    i=i-1
    loc=a[i]+2
    while i<n and a[i]<=loc:
        i=i+1
print(count)
    
