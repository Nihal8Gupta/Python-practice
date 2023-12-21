def Index(l,t):
    if len(l) == 0:
        l.append(t)
        return 0
    else:
        for i in range(len(l)-1):
            if l[i] < t <= l[i+1]:
                l.insert(i+1,t)
                return(i+1)
        else:
            if t > max(l):
                l.append(t)
                return len(l)-1
            else:
                l.insert(0,t)
                return 0

l=[1,2,3,6,7]
target = 1
print(Index(l,target))
#Second Approach
l=[1,2,3,6,7]
target = 1
l=l+[target]
l.sort()
print(l.index(target))