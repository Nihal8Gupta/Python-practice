n=5
star=1
d=1
t=True
for i in range(1,n+1):
    for st in range(star):
        if t:
            print(d,end=' ')
            d+=1
            t=False
        else:
            print('*',end=' ')
            t=True

    print()
    star+=1