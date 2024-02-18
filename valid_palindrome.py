def isPalindrome(s):
    s = [ i for i in s.lower() if i.isalpha() or i.isdigit()]
    s = "".join(s)
    return s == s[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))