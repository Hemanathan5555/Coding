a = [5, 10, 20, 15, 7, 25, 30, 10]
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        print(i)
    else:
        pass
