n = 8
l = list(range(1,n+1))
for i in range(len(l)):
    if sum(l[0:i+1])==sum(l[i:]):
        print(l[i])
        break
else:
    print(-1)