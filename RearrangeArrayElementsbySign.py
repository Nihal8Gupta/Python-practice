nums = [3,1,-2,-5,2,-4]
pl = [i for i in nums if i > 0]
nl = [i for i in nums if i < 0]
l = len(pl)
nums = []
for i in range(l):
    nums.append(pl[i])
    nums.append(nl[i])
print(nums)