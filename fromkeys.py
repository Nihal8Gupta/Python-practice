print("Program for counting all index of given string:-")
s=input("Enter the string for keys=")
d={}.fromkeys(s,[])
c=0
for i in s:
    if i not in d:
        d[i]=c
    else:
        d[i]=d[i]+[c]
    c+=1
print("Elements with index=",d)