#WAP all odd numbers in given number
s='52'
l=len(s)

for i in range(l-1,0,-1):
  
    if int(s[i])%2!=0:
        print(s[0:i+1])
        break
else:
    if int(s[0])%2==1:
        print(s[0])
    else:
        print("")