# Alternative binary string
def alter(s,b):
    count = 0
    for i in range(0,len(s),2):
        if s[i:i+2] != b and  len(s[i:i+2]) == 2:
            if s[i] != b[0]:
                count +=1
                
            elif s[i+1] != b[1]:
                count += 1
                
        elif s[i:i+2] != b and  len(s[i:i+2]) == 1:
            if s[i] != b[0]:
                count +=1
    return count
s = '"10010100"'
f = alter(s,'01')
s = alter(s,'10')

      
print(min(f,s))