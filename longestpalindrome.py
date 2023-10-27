def longestPalindrome(s: str) -> str:
        
        j=len(s)
        i=0
        while i<=len(s)-j+1:
            if s[i:i+j]==s[i:i+j][::-1]:
                return s[i:i+j]
            i+=1
            if i>len(s)-j:
                i=0
                j-=1
            if j==1:
                return s[0]
s=input()
res=longestPalindrome(s)
print(res)