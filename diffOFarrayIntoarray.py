#Divide Array Into Arrays With Max Difference
nums = [1,3,4,8,7,9,3,5,1]
k = 2
nums.sort()
n = len(nums)
result = []

for i in range(0, n - 2, 3):
    if nums[i + 2] - nums[i + 1] <= k and nums[i + 1] - nums[i] <= k and nums[i + 2] - nums[i] <= k:
        result.append([nums[i], nums[i + 1], nums[i + 2]])
    else:
        break
print(result)