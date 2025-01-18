a=[2,3,4,7,8]
count=0
for i in a:
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i)
        count=0
    else:
        count=0
        
    
