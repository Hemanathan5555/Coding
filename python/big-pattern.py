a=7
for i in range(0,a+1):
    for j in range(0,a-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("* ",end="")
    print()
