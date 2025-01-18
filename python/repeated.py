a="AABBB"
k=list(a)
count=0
for i in range(0,len(k)):
    if k[i]==k[i+1]:
        count=count+1
    if i==len(a)-2:
        break
print(count)
    
    
    
