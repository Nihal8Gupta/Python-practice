s = "abcxmkn"
d={}

for i in range(len(s)):
    if s.count(s[i]) > 1:
        if s[i] not in d :
            d[s[i]] = [i]
        else:
            d[s[i]] += [i]
if d:
    r = min(d.values())
    print(r)
    for i in d:
        if d[i][-1]-d[i][0] > r[-1]-r[0]:
            r=d[i] 
    print(d,r)
    print(r[-1]-r[0]-1)
else:
    print(-1)