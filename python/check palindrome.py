a="racecar"
k=len(a)-1
count=0
for i in range(0,len(a)):
    if a[i]==a[k-i]:
        count=count+1
    else:
       pass
if count==len(a):
    print("its a palindrome")
else:
    print("no its not a palindrome ")
