#WAP to check valid brackets
s='[{}}'
d={']':'[',")":'(','}':'{'}
l=[]
for i in s:
    if i in '({[':
        l.append(i)
    else:
        if len(l)>0 and d[i] ==l[-1]:
            l.pop(-1)
        else:
            print(False)
            break
else:
    if l:
        print(False)
    else:
        print(True)