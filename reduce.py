#WAP to print max value by reduce method

from functools import reduce
l=eval(input())
print(reduce(lambda x,y:x if x>y else y,l))