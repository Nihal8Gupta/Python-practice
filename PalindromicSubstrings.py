s = 'aaa'
total = 0
n = len(s)
for i in range(1, n):
    for j in range(n-i):
        if s[j:j+i]==s[j+i:j:-1]:
            total+=1
print(total+n)