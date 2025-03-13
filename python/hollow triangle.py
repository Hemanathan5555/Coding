n=5
for i in range(n):
    for j in range(n*2-1):
        if j==n-i-1 or j==n+i-1 or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
        
