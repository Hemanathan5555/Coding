l = []
r = 3
c = 3
for i in range(r):
    temp = []
    for j in range(c):
        a = int(input())
        temp.append(a)
    l.append(temp)
for i in l:
    for j in i:
        print(j,end=" ")
    print()    
