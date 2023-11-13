#Sort Vowels in a String
s = "lEetcOde"
l=len(s)
vowel='aioueAIOUE'
temp=[]
for i in range(l):
    if s[i] in vowel:
        temp.append(s[i])
        s=s.replace(s[i],' ',1)

temp.sort()
print(s,temp)
for i in range(l):
    if s[i]==' ':
        s=s.replace(' ',temp.pop(0),1)
print(s)