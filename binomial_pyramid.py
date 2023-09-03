#WAP to print Binomial

print('-: Binomial pyramid :-')
from math import perm,factorial
n=int(input("Enter row="))
star=1
space=n-1
d=0
for i in range(1,n+1):  #for rows

    for sp in range(1,space+1):  #for spaces
        print(' ',end=' ')
    for st in range(0,star):
        print(perm(d,st)//factorial(st),' ',end=' ')
           
    print()
    d+=1                            
    space-=1
    star+=1