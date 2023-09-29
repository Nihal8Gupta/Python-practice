s="leet2code3"
i=0
k=10
while i<len(s):
    if s[i].isdigit():
        d=s[i]
        s=s.replace(s[:i+1],s[:i]*int(s[i]),1)
        i=i*int(d)-1
    if i>=k-1:
        print(s,'Ans:',s[k-1])
        break
    i+=1