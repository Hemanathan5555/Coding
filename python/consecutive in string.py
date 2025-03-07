a="10110111011"
s=""
for i in a:
    if i=="1":
        s=s+i
    else:
        print(s)
        s=""
if s:
    print(s)
