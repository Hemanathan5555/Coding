a="defghijklmnopqrstuvwxyzabc"
b="thereisanapplepwnasjskfvck"
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if  b[i]==a[j]:
            l=j+3
            
            if l<len(a):
                print(a[l])
                
            else:
                l=l-len(a)
                print(a[l])
                
        else:
            pass
            
