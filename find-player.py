# Find Players With Zero or One Losses
from collections import Counter
matches = [[2,3],[1,3],[5,4],[6,4]]
los = Counter([ i[1] for i in matches])
s=set()
res=[[],[]]
for i in matches:
    s.add(i[0])
    s.add(i[1])
for i in s:
    if los.get(i,0)==0:
        res[0].append(i)
    elif los.get(i,0)==1:
        res[1].append(i)
print(res)