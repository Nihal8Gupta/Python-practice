from collections import Counter
words = ["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]
if len(words) > 1:
    words.sort(key=len)
    d = Counter(words[0])
    for i in range(1,len(words)):
        dn=Counter(words[i])
        for j in dn:
            d[j] = d.get(j,0)+dn.get(j,0)
    result =list(filter(lambda i: True if d[i]%len(words)==0 else False,d))
    
    if len(d) == len(result):
        print(True)
    else:
        print(False)
else:
    print(True)