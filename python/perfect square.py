num=28
sum=0
for i in range(1,28):
    if num%i==0:
        sum=sum+i#adding integers if it is divisble by 28
if num==sum:
    print("true")
else:
    print("false")
