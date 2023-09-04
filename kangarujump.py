print("Kangaroo jump\nCondition :-")
print("x2>x1  and v2>v1")
x1=int(input("Enter  first kangaroo starting point="))
v1=int(input("Enter  first kangaroo jump distance="))
x2=int(input("Enter  second kangaroo starting point="))
v2=int(input("Enter  second kangaroo jump distance="))

while x1<=1000 and x2<=1000:
    x1+=v1
    x2+=v2
    if x1==x2:
        print("YES")
        break
else:
    print('NO')