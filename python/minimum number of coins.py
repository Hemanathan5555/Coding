a=[50,20,10,2,1]
k=93
count=0
for i in a:
    while i<=k and k>0:
        k=k-i
        count=count+1
print(count)
        
