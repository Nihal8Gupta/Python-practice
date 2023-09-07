s='aaabccddd'
print(s)
i=0
while i<len(s):
    ns=''
    for j in range(len(s)-1):
        if s[j:j+2]==s[j:j+2][::-1]:
            if j==0:
                ns+=s[j+2:]
                s=ns
                break
            else:
                ns+=s[:j:]+s[j+2::]
                s=ns
                break
    i+=1
if len(s)>0:
    print(s)
else:
    print('Empty String')
#aaabccddd
#abccddd
#abddd
#abd
