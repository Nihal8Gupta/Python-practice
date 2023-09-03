#WAP to print pyramid of alphabate
n=int(input("Enter row="))
star=1
space=n-1
for i in range(1,n+1):  #for rows
    d=64+i
    for sp in range(space):  #for spaces
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(d),end=' ')
        if st<star//2+1:
        
            d-=1
        else:
            d+=1   
           

    print()                             #for next line
    space-=1
    star+=2