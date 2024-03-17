def findNearest(N,arr,X):
    for i in range(N):
        for j in range(len(arr[i])):
            if arr[i][j] % X != 0 and arr[i][j] < X:
                arr[i][j]=0
            elif arr[i][j] % X == 0 and arr[i][j] < X:
                arr[i][j]=X
            elif arr[i][j] % X != 0 and arr[i][j] > X:
                arr[i][j]=6
    return arr
arr= [[1,8],[3,6]]
print(findNearest(2,arr,3))