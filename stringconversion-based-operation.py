#WAP to convert alphabate into based operation if alphabate is vowel
#if alphabate is vowel then take its index position and multiply with 100
#After that add all prime numbers between 1 to what you get in second line
#And check if sum is in single digit then store this digit in place of that alphabate otherwise add that each digit until that number convert into single digit 
 
def isPrime(N):
    if N>1:
        for i in range(2,N//2+1):
            if N%i==0:
                return False
        else:
            return True
    else:
        return False
    
def sNumber(N):  #sum of digit
    add=0
    while N!=0:
        r=N%10
        N=N//10
        add+=r
    return add

        
def replace(s):
    w=''
    for i in range(len(s)):
        if s[i] in "aioueAIOUE":
            
            sum=0
            for n in range(1,i*100+1):
                if isPrime(n):
                    sum+=n
            while sum>9:
                sum=sNumber(sum)

            w+=str(sum)
        else:
            w+=s[i]
    return w
result=replace(input())      
print(result)
