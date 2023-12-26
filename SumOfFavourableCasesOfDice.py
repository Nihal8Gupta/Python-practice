#WAP to find sum of favourable case of dice
from itertools import combinations
n = 3  #dice
k = 6  #faces
target = 17   #sum=17
f=list(range(1,k+1))
l=[]
count = 0
for i in range(n): l.extend(f)
l=sorted((set(combinations(l,n))))
for i in l:
    if sum(i)==target:
        count += 1
print(count)