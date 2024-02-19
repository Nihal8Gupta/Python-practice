def isPowerOfTwo(n):
    i=0
    while True:
        if n == 2**i:
            return True
        elif n > 2**i:
            i += 1
        else:
            return False
print(isPowerOfTwo(16))
