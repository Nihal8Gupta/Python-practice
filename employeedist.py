#Employee Distance
n=int(input("Enter the number of elements="))
l=[]
for i in range(n):
    e=int(input(f"Enter the {i+1} Employee="))
    l.append(e)
    
for i in l:
    print(i,end=" ")
    

LL=int(input("\nEnter the lower lim="))
UL=int(input("Enter the Upper lim="))
for i in l:
    if i in range(LL,UL+1):
        print(i,end=" ")
