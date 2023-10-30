#Leetcode sort numbers by bits
from functools import reduce
arr = [100,100]
arr=[10,100,1000,10000]
arr.sort()
d={}
for i in arr:
    if bin(i).count('1') not in d:
        d[bin(i).count('1')]=[i]
    else:
        d[bin(i).count('1')]+=[i]
key=sorted(d)
d={i:d[i] for i in key}
print(d)
d=list(reduce(lambda x,y:x+y,d.values()))
print(d)