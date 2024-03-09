d={}
for i in range(ord('A'),ord('Z')+1):
    if len(d)==0:
        d[chr(i)]=1
    elif len(d)==1:
        d[chr(i)]=2
    else:
        d[chr(i)] = d[chr(i-1)]+d[chr(i-2)]
print(d)