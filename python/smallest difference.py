a=[-59,-36,-13,1,-53,-92,-2,-96,-54,75]
mini=1000
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        c=abs((a[i])-(a[j]))
        if c<mini:
            mini=c
        else:
            pass
print(mini)
