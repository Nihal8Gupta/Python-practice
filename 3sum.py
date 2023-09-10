#WAP to print all three numbers whose summation is 0
l=[-1,0,1,2,-1,-4]
if l.count(0)==len(l):
    print([0,0,0])
else:
    nl=[]
    for i in range(len(l)-2):
        add=l[i]
        for j in range(i+1,len(l)-1):
            add=l[i]+l[j]
            for k in range(j+1,len(l)):
                if sum([add,l[k]])==0:
                    nl.append([l[i],l[j],l[k]])
                    break
    print(nl)