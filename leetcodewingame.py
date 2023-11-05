#Find the Winner of an Array Game
arr = [2,1,3,5,4,6,7]
k = 2
count={}
while True:
    if arr[0]>arr[1]:
        if arr[0] not in count:
            count[arr[0]]=1
        else:
            count[arr[0]]+=1

        arr.append(arr.pop(1))
    else:
        if arr[1] not in count:
            count[arr[1]]=1
        else:
            count[arr[1]]+=1

        arr.append(arr.pop(0))
    if k in count.values():
        break
count={ v:k for k,v in count.items()}
print(count)
mx=max(count)
print(count[mx])