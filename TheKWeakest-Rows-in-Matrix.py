mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k=3
d=[]
for i in range(len(mat)):
    d.append([mat[i].count(1),i])
d.sort()
l=[]
for i in range(k):
    l.append(d[i][1])
print(d,l)