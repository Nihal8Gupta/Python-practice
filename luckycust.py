def OrderID(token):
    n1=1
    n2=1
    for i in range(token-1):
        n1=n1+n2
        n1,n2=n2,n1
    return n1
    
def Enter():
    token=int(input("Enter the token="))
    t=OrderID(token)
    print('Lucky customer OderID=',t)
Enter()