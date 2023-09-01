#WAP to print transpose of matrix
r=int(input("Enter the row of Matrix="))
l=[]
t=[]
for row in range(r):
    l.append(eval(input(f"Enter the elements for {row+1}st row in the list format=")))

for i in range(len(l[0])):
    t.append([])
    
for row in range(len(l)):
    for col in range(len(l[0])):
        t[col].append(l[row][col])
print(" -: Transpose of matrix :-")        
for row in t:
    print(row)
