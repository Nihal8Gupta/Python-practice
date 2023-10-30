#WAP for Binary Search
arr=[20,10,8,44,12,30,11]
target=int(input("Enter the target value="))
arr.sort()
left,right=0,len(arr)-1
print(arr)
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print(arr[mid])
        break
    elif arr[mid]<target:
        left=mid
    else:
        right=mid
    print(mid)