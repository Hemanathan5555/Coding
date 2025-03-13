n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if n==i or n//i==n or j-1==0 or j+1==n+1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
