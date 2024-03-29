def interpolation(l,low,high,user):
    mid=low+((high-low)//(l[high]-l[low]))*(user-l[low])
    if low<=high and l[low]<=user<=l[high]:
        if l[mid] > user:
            high = mid-1
        elif l[mid] < user:
            low = mid+1
        elif l[mid]==user:
            return mid
        return interpolation(l,low,high,user)
    return -1

l=[9,3,6,8,1,7,0]
l.sort()
print(interpolation(l,0,len(l)-1,7))