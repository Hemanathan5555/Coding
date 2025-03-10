a=[1,2,3,4,10,20,30,40,100,200]
k=4
mini=1000
for i in range(0,len(a)):
    s=max(a[i:k])-min(a[i:k])
    if s<mini:
        mini=s
    k=k+1
    if k>len(a):
        break
print(mini)
