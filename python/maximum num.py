a = [1,4,5,3,2]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):#adding first number with every number following after it
        if a[i]+a[j]==6:
            #second loop runs and add second and follwing num it
            #it runs till length a
            print(i+1,j+1)
        else:
            pass
        if i==len(a)-1:#it break when last num in array comes for operation
            break
