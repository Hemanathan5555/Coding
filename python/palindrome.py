s="sas"
b=""
k=-1
for i in range(0,len(s)):
    b=b+s[k]#ads character from the last
    k=k-1
if b==s:
    print("its a palindrime")
else:
    print("its not a palindrome")
