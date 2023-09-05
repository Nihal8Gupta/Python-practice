#WAP to print lengthy distinct word
s='PWWKEWA'
l=''
w=''
for i in range(len(s)-1):

    for j in range(i+1,len(s)):
        if s[j] not in s[i:j]:
            w=s[i:j+1]
        else:
            break
    if len(w)>len(l):
        l=w

print(l)