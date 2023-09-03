#WAP to print fibon in Greater than symbol
star=1
space=0
n1=2
n2=3
n=int(input("Enter the nth term="))
l=[]
for i in range(n):       
    l.append(n1)
    n1=n1+n2                 
    n1,n2=n2,n1  

for i in range(1,n+1):
    for sp in range(1,space+1):
            print(' ',end=' ')
    
    for st in range(1,star+1):
            print(l[i-1],end=' ')
       
    print()
    
    if i<n//2+1:
        space+=1
        
    else:
        space-=1