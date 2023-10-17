a,b,c=0,1,1
n=8
i=0
print(a,b,c,end=' ')
while i<n:
    t=a+b+c
    a=b
    b=c
    c=t
    print(t,end=' ')
    i+=1
