arr = [2,1,3,5,4,6,7]
arr=[3,1,2]
k = 10
c = 0
winner = arr.pop(0)

for i in arr:
    if i>winner:
        winner = i
        c = 1
    else:
        c += 1
    if c == k:
        print(winner)
        break
print(winner)