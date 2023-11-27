#IBM test
def decryptMessage(encryptedmessage,keyPhrase):
    decrypted=[]
    word =(encryptedmessage+' '+keyPhrase).split()
    if len(word)%2==0:
        for i in range(len(word)//2):
            if not word[i].islower() or not word[i].isalnum():
                return 'Invalid input'
            else:
                d=len(word[len(word)-1-i])
                w=''
                if d%2==0:
                    for j in word[i]:
                        asc=ord(j)-d
                        if asc < 97:
                            asc=abs(ord('a')-asc)
                            asc=123-asc
                        w+=chr(asc)
                else:
                    for j in word[i]:
                        asc=ord(j)+d
                        if asc > 122:
                            asc=asc-ord('z')
                            asc=96+asc
                        w+=chr(asc)
                decrypted.append(w)
    else:
        return 'Invalid input'
    return ' '.join(decrypted)
print(decryptMessage('qiix gz clro','one orange ball'))