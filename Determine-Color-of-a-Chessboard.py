#Determine Color of a Chessboard Square
coordinates = "b2"
white=True
black=False
temp={}
for i in range(97,105):
    if i%2==0:
        temp[chr(i)]=white
    else:
        temp[chr(i)]=black
print(temp)
c1=coordinates[0]
c2=int(coordinates[1])
if c2%2!=0:
    print(temp[c1])
else:
    print(not temp[c1])