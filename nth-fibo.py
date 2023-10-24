#WAP to print nth fibonacci number
n=int(input())
a=0
b=1
if n>1:
    for i in range(n):
        a+=b
        a,b=b,a
        if i==n-1:
            print('r=',a)