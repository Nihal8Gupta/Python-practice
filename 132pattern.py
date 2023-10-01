nums=[-2]
i=0
j=i+1
k=j+1
while len(nums)>2:
    if k==len(nums):
        i+=1
        j=i+1
        k=j+1
    print(i,j,k)

    if nums[k] < nums[j] and nums[k] > nums[i]:
        print(True)
    if i==len(nums)-3:
        break
    k+=1
else:
    print(False)
    
