#Minimize maximize sum of pair
nums = [3,5,2,3]
nums.sort()
l=len(nums)
temp=nums[0]+nums[l-1]
for i in range(1,l//2):
    
    if temp<nums[i]+nums[l-i-1]:
        temp=nums[i]+nums[l-i-1]
print(temp)