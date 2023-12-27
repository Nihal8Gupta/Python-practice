colors = "aaabbbabbbb"  #3,5,5,3,4,5,1
c=list(colors)
print(c)
neededTime = [3,5,10,7,5,3,5,5,4,8,1]
count = 0
i=0
while i < len(c)-1:
    if c[i] == c[i+1]:
        if neededTime[i] < neededTime[i+1]:
            c.pop(i)
            count += neededTime.pop(i)
           
        else:
            c.pop(i+1)
            count += neededTime.pop(i+1)
        i -= 1
    i += 1
print(count)