arrival =  [900, 940, 950, 1100, 1500, 1800]
d = [910, 1200, 1120, 1130,1400,1200]
count=0
i=0
j=1
n=len(d)
while j<len(d):
    if d[i]>d[j]:
        count=count+1
        j=j+1
    else:
        i=j
        j=j+1
print(count)
