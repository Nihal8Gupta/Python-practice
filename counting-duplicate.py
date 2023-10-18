def dictionary(textInput):
    sent=textInput.split()
    res=[]
    for i in sent:
        if sent.count(i)>1:
            if i not in res:
                res.append(i)

    return ' '.join(res) if len(res)!=0 else 'NA'
    
r=dictionary('cat batman latt matter cat matter cat')
print(r)