a="DDUUDDUU"
#here we have to find the valley d is -1 and u is 1
#a  valley will occur when it is zero
b=[]
count=0
for i in a:
    if i=='D':#if i is D means
        count=count-1#count-1 it will get iterate
        if count==0:
            b.append(0)
    else:
        count=count+1#count+1 it will get iterate
        if count==0:
            b.append(0)
print(b.count(0))
