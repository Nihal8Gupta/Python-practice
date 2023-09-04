print("Average:--")
n=int(input("Enter the number of values="))
sum=0
for i in range(n):
  v=int(input(f"Enter the {i+1} value="))
  sum=sum+v

print(f"Average of {n} numbers=",sum/n)
