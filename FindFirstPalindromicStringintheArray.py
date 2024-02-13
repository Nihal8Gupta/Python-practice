def firstPalindrome(self, words):
    for w in words:
        if w == w[::-1]:
            return w
    else:
        return ''
print(firstPalindrome(['aab','add','ikskl','poop']))