def g(n):
    for i in range(1,n):
        print(f'{i} * {i} =',end=' ')
        yield i**2

o=g(4)
for i in o:
    print(i)