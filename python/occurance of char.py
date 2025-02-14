a="abcac"
n=10
for i in range(0,n):
    a=a+a
    if len(a)>n:
        a=a[:10]
        break
print(a.count("a"))
