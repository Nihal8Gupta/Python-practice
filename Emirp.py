#WAP to check number is Emirp or not with nested function
def isEmirp(N):
    def isPalindrome(N):
        d=N
        rev=0
        while d!=0:
            r=d%10
            d=d//10
            rev=rev*10+r
    
        def isPrime(Num):
            if Num>1:
                for i in range(2,Num//2+1):
                    if Num%i==0:
                        return False
                else:
                    return True
            else:
                return False
    
        if N!=rev:
            if isPrime(N) and isPrime(rev):
                return True
            else:
                return False
        else:
            return False
    return isPalindrome(N)

print(isEmirp(int(input())))