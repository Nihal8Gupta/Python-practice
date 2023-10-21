def S(n,n1,l):
    s=1
    while s<=l:
        yield s,n
        s+=1
        n+=n1
        n,n1=n1,n
s=S(0,1,10)
for i in s:
    print(f"{i[0]}. {i[1]}") 