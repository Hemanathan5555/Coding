a=[6,5,2]
k=2
s=1
sums=0
for i in range(0,len(a)):
    count=a[i]*s
    sums=sums+count
    if (i+1)%2==0:
        s=s+1
print(sums)
        

        
    
