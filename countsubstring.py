# implement the functionality of count method.
s=input ('enter the string=')
sub=input ('enter the substring=')
c=0
for i in range(len(s)-len(sub)+1):
    print(s[i:i+len(sub)])
    if s[i:i+len(sub)]==sub:
        c+=1
print(c)