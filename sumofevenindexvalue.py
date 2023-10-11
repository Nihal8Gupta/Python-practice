#WAP to print sum of all even index value until it having single value
def evan(l,d):
    for i in range(len(l)-1,-1,-1):
        if i%2==0:
            d.append(l.pop(i))
    return (l,d)

n=int(input())
l=list(range(1,n+1))
print(l)
d=[]
while 1<len(l):
    t=evan(l,d)
    l=t[0]
    
print(l,d)
print("Sum",sum(d))

