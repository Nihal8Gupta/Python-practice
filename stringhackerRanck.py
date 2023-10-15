s='coOL dog'
i=0
w=s.split()
n=s[0]
while i in range(len(s)-1):
    if s[i+1].isalpha():
            if s[i].lower()>s[i+1].lower():
                print('later')
                n+=s[i+1].lower()
            if s[i].lower()<s[i+1].lower():
                print('earli')
                n+=s[i+1].upper()
            if s[i].lower()==s[i+1].lower():
                print('Equal')
                n+=s[i+1]
    else:
        n+=s[i+1]
        i+=1
        n+=s[i+1]
    i+=1
print(n)