#Find Unique Binary String (leetcode)
def conversion(l):
    string=''
    for i in l:
        string+=str(i)
    return string
from itertools import combinations_with_replacement
nums = ["00","01"]
comb=list(combinations_with_replacement((0,1),len(nums[0])))

for i in comb:
    if i==i[::-1]:
        temp=conversion(i)
        if temp not in nums:
            print(temp)
            break
    else:
        temp=conversion(i)
        if temp not in nums:
            print(temp)
            break
        temp=conversion(i[::-1])
        if temp not in nums:
            print(temp)
            break