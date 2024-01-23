arr = ["ab","cd","cde","cdef","efg","fgh","abxyz"]
new = sorted(arr,key=len)
print(new)
if len(arr)==1:
    print(len(new[0]))
elif len(arr)==0:
    print(0)
else:
    c=''
    for i in range(-1,-len(new)-1,-1):
        if len(new[i]) == len(set(new[i])):
            for j in new[i]:
                if j in c:
                    break
            else:
                c += new[i]
print(c,len(c))