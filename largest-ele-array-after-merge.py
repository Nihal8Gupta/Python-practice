def cal(l):
    for i in range(-1,-len(l),-1):
        if l[i-1]<=l[i]:
            return True,i-1
    else:
        return None

nums = [2,3,7,9,3]
ind=int(input('Index='))
if 0<=ind<len(nums)-1:
    nums[ind+1]+=nums[ind]
    nums.pop(ind)

flag=True
while flag:
    ans=cal(nums)
    if ans:
        ind=ans[1]
        nums[ind+1]+=nums[ind]
        nums.pop(ind)
    else:
        
        flag=False
    print(nums)
print(max(nums))
'''
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n-1,0,-1):
            if nums[i-1]<=nums[i]:
                nums[i-1]=nums[i-1]+nums[i]

        return nums[0]
'''