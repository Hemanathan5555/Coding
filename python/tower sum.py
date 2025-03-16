a=[7, 12, 20, 30, 40]
k=len(a)//2
for i in range(0,k):
    count=0
    c=a[i]+6
    count=count+c
    print(count)
for i in range(k+1,len(a)):
    count=0
    c=a[i]-6
    count=count+c
    print(count)
    
    
