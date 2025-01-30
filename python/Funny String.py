a="0100101010"
k=0
b=2
count=0
for i in range(0,len(a)):
    if a[k]=='0' and a[b]=='0':#comparing first and third element
        a=a[:k]+'1'+a[k+1:]
        k=k+3
        b=b+3
        count=count+1#counting the number of changes done
    elif a[k]!='0' and a[b]!='0':#comparing after the iteration
        k=k+1
        b=b+1
    else:
        pass
    if b>len(a):
        break
print(count)
