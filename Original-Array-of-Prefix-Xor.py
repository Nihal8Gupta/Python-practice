pref = [5,2,0,3,1]
res=[pref[0]]
for i in range(1,len(pref)):
    res.append(pref[i]^pref[i-1])
print(res)
'''
 pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
'''