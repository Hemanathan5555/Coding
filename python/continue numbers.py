a=[(1,2),(2,3),(5,7),(3,6),(8,9)]
maz=0
count=0
for i in a:
    for j in i:
        if i[0]>=maz:
            count=count+1
            maz=i[1]
        else:
            maz= i[1]
print(count)
