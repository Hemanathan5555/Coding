a=[2,2,3,4,56]
score1=a[0]
score2=a[0]
count=0
count1=0
for i in a:
    if i>score1:
        count=count+1
        score1=i
    elif i<score2:
        count1=count1+1
        score2=i

print(count)
print(count1)
        
    
