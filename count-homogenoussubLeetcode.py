#Count Number of Homogenous Substrings (leetcode)
s = "abbcccaa"
mod = 10**9+7
c = 1
prv = s[0]
res = 1
for ch in s[1:]:
    if ch == prv:
        c+=1
    else:
        c = 1
        prv = ch

    res+=c
    res %= mod
print(res)