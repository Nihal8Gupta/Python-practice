#WAP to print pattern

#WAP to print Greater than symbol
n=int(input("Enter the row="))
star=1
space=0
t=1
for i in range(1,n+1):
    for sp in range(1,space+1):
            print(' ',end=' ')
    
    for st in range(1,star+1):
            print(t,end=' ')
       
    print()
    
    if i<n//2+1:
        space+=1
        t+=2
    else:
        space-=1
        if i>n//2+1:
             t-=2
        else:
            t-=1