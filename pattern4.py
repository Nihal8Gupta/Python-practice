#WAP to print diamond
n=int(input("Enter row=")) #5
star=1
space=n//2

for i in range(1,n+1):
    d=star//2+1
    for sp in range(1,space+1):  #for spaces
        print(' ',end=' ')
    for st in range(1,star+1):      #for stars
        print(d,end=' ')
        if i%2!=0:
            if st<star//2+1:
                d-=1
            else:
                d+=1 
        else:
            if st<star//2+1:
                d+=2
            else:
                d-=2
    print()    
    if i<=n//2:                         
        space-=1
        star+=2
        
    else:   
        space+=1
        star-=2