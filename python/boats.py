w = [8,2,6,4]
k = 10
count=0
n=0
while n<len(w):
    count=count+1
    m=0
    while m<k and m+w[n]<=k :
        m=m+w[n]
        n=n+1
        if n==len(w):
            break
print(count)
