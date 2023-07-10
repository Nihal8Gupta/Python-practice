import math
print("# Program of Armstrong number #")
c=100
for k in range (c):
 num=int(input("Enter the number="))
 arms=num
 j=100
 s=0
 for i in range(j):
  n=num%10
  if num==0:
   break
  num=int(num/10)
  s=int(s+math.pow(n,3))
 
 if s==arms:
    print(f"{arms} is a Armstrong number.")
 else:
    print(f"{arms} is not a Armstrong number.")
 op=str(input("*Press YES for further operation\n*Press NO for terminate the program\nPress here="))
 if op=="YES":
  print("Successful operation")
 else:
   print("Quit")  
   break
