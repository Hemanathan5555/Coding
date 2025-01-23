first=0
second=1
a=0
while a<6:#giving a condition
    print(first)
    temp=first#storing the first value in the temp variable 
    first=second
    second=temp+second#second updated into sum of first and second   
    a=a+1
