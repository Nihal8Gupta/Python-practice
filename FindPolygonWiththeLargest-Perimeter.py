def largestPerimeter(self, nums):
    nums.sort()
    p=0
    sum=nums[0]+nums[1]
    for x in nums[2:]:
        if sum>x:
            p=sum+x
        sum+=x
    return -1 if p==0 else p
nums = [1,12,1,2,5,50,3]
print(largestPerimeter(nums))