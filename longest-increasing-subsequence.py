#Longest increasing subsequence
nums = [3,4,-1,0,6,2,3]  #[10,9,2,5,3,7,101,18]
l = [1]*len(nums)
for i in range(1,len(nums)):
    for j in range(len(nums)):
        if j < i:
            if nums[j] < nums[i] :
                if l[j] == l[i]:
                    l[i] += 1
                elif l[j] > l[i]:
                    l[i] += l[j]
        else:
            break
print(max(l))