s = "anagram"
t = "mangaar"
nst = ''
for i in set(t):
    if i in s:
        if t.count(i) == s.count(i):
            nst += i*s.count(i)
        else:
            if t.count(i) > s.count(i):
                nst += i*s.count(i)
            else:
                nst += i*t.count(i)

print(nst,len(s)-len(nst))