a=['1892','1112','1912','191']
k=[]
for i in a:
    k.append(max(i))
z=max(k)
for i in a:
    z=max(k)#getting max value of the array
    p=len(i)-1
    for j in range(0,len(i)):#here we taking the len of i in a
        if i[0]==z and i[p]==z:#so the first and last are equal means it will pass
            pass
        elif i[j]==z:#if the max is in center it replace by x
            i=i[:j]+'x'+i[j+1:]
        elif i[j]!=z:#if there is no max value in the string pass
            pass
    print(i)
    






