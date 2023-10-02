def search(s,t):
    for i in range(len(s)-2):
        if s[i:i+3:]==t:
            s=s[0:i+1:]+s[i+2::]
            print(s)
            return (True,s)
    else:
        return (False,s)
colors='AAAAABBB'
s=True
while True:
    if s:
        if colors.count('AAA')!=0:
            t=search(colors,'AAA')
            if t[0]:
                s=False
                colors=t[1]
            else:
                print('BOB win')
                break
        else:
            print('BOB win')
            break
    else:
        if colors.count('BBB')!=0:
            t=search(colors,'BBB')
            if t[0]:
                s=True
                colors=t[1]
            else:
                print('Alice win')
                break
        else:
            print('Alice win')
            break