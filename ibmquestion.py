def tableOfContent(text):
    res = []
    cap = 0
    for t in text:
        if t.startswith('##'):
            res.append(f'{cap}.{sec}.'+ t.strip('##'))
            sec+=1
        elif t.startswith('#'):
            cap+=1
            res.append(f'{cap}.'+ t.strip('#'))
            sec = 1
        
    return res

result = tableOfContent(['# Cars',"## Sedan",'## So','# Bo','## Jo','# Nil', '## Ho'])
print('\n'.join(result) )   