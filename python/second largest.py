a=[35,6,8,34,99,100]
largest=0
second=0
for i in a:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print(second)
