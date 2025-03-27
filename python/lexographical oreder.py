S = "dcab" 
mini =S
k=""
for i in range(0,len(S)-1):
    for j in range(i+1,len(S)):
        k=S[i]+S[j]
        if k<mini:
            mini=k
            k=""
        else:
            k=""
print(mini)
        
        
