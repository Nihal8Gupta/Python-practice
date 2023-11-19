#Reduction Operations to Make the Array Elements Equal
#[5,1,3] ans=3, [1,1,1] ans=0
nums = [1,1,2,2,3]
n = len(nums)
nums.sort(reverse=True)
ans = 0
for i in range(n-1):
    if nums[i] > nums[i+1]:
        ans += i+1
print(ans)