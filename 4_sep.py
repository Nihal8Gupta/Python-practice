#WAP to print given alphabate with how many times it is present continously
s="aaabbcda"
sub=""
c=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1 
    else:
        sub+=str(c)+s[i]
        c=1
sub+=str(c)+s[i+1]     
print(sub)