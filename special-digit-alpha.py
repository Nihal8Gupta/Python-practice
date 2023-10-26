#WAP for counting digits,alphabetes,special char in the given string without using meyhods
'''
S=input("Enter the string=")
d=a=sc=0
for i in S:
    if i in '0123456789':  
        d+=1
    elif  ord(i) in range(65,90) or ord(i) in range(97,122):
        a+=1
    else:
        sc+=1
            
print("number of digit=",d)
print("number of alphabet=",a)
print("number of special char=",sc)
'''

'''
S=input("Enter the string=")
d=a=sc=0
for i in S:
    if i in '0123456789':  
        d+=1
    elif  i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        a+=1
    else:
        sc+=1
            
print("number of digit=",d)
print("number of alphabet=",a)
print("number of special char=",sc)

'''
S=input("Enter the string=")
d=a=sc=0
for i in S:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'): 
        a+=1
print(a)
