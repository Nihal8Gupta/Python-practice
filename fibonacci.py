
#Fibonacci : 0,1,1,2,3,5,8,13,21....nth term
print('Fibonacci : 0,1,1,2,3,5,8,13,21....nth term')
n1=int(input("Enter the 1st term="))
n2=int(input("Enter the 2nd term="))
n=int(input("Enter the nth term="))
Sum=0
for i in range(n):
    if i==n-1:
        print(n1)   #n1=0
    else:
        print(n1,end=',')        #n1=0,1,1,2,3..... 
    Sum+=int(n1)    
    n1=n1+n2                  #(n1=1,n2=1),(n1=2,n2=1),(n1=3,n2=2),(n1=5,n2=3)
    n1,n2=n2,n1              #(n1=1,n2=1),(n1=1,n2=2),(n1=2,n2=3),(n1=3,n2=5)
  
print("Sum of series=",Sum)    
