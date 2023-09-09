#WAP to print sum of respective elements
l=[[1,4],[2,5,8,11,13],[3,6,14]]
nl=[]
x=len(max(l,key=len))
print('Given list:',l)
for i in range(x):
    add=0
    for j in range(x):
        if x>i:
            if len(l)>j and len(l[j])>i:
                add+=l[j][i]
    nl.append(add)
print(nl)