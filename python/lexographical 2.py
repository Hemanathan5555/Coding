S = "fgbadce" 
mini=S
k=3
b=k-1
for i in range(0,len(S)-2):
    for j in range(i+2,len(S)):
        m=S[i:b]+S[j]
        if m<mini:
            mini=m
            m=""
        else:
            m=""
    b=b+1
print(mini)
        
    
