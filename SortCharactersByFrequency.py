from collections import Counter
from functools import reduce
s = "Aabb"
c = Counter(s)
d = []
for i in c:
    d.append([c[i],i])
d = sorted(d,reverse=True)
c=''
for i in d:
    c += i[0]*i[1]
print(c)