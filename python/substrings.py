a="abba"
for i in range(0,len(a)):
    for j in range(i+1,len(a)+1):
        c=a[i:j]
        k="".join(c)
        print(k,end=" ")
print()
