l=[[1,2,3],[20,11],[100]]
nl=[]
print('Given list:',l)
for i in range(len(l)):
    add=0
    for j in range(len(l)):
        if len(l[i])>=j+1:
            add+=l[j][i]
    nl.append(add)
print('After Opertaion:',nl)