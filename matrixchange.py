l=[[1,2,3],[6,0,0],[2,8,1]]
x=[]
y=[]
print('Given Matrix :')
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j],end=' ')
    print()
for i in range(len(l)):
    for j in range(len(l)):
        if 0==l[i][j]:
            x.append(i)
            y.append(j)

for i in range(len(l)):
    for j in range(len(l)):
        if i in x or j in y:
            l[i][j]=0
            
print('After operation :')
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j],end=' ')
    print()