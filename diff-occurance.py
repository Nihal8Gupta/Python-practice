from collections import Counter
arr = [1,2,2,1,1,3]
c=Counter(arr)

for i in c.values():
    if (list(c.values())).count(i) != 1:
        print(False)
        break
else:
    print(True)