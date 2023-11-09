#Count Number of Homogenous Substrings
s = "abbcccaa"
i=0
j=1
dict_count={}
List=[]
while True:
    List.append(s[i:j+i])
    if i <len(s)-j:
        i+=1
    else:
        i=0
        j+=1
    if j>len(s):
        break

temp=list(set(s))
print(temp)
i,j=0,1
while i<len(temp):
    sub=temp[i]*j
    if sub in List:
        dict_count[sub]=List.count(sub)
        j+=1
    else:
        i+=1
        j=1
print(dict_count)
print(sum(dict_count.values()))