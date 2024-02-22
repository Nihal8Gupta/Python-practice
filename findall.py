#finditer it will find the pattern and return iter object
import re
pattern  = re.compile('hello')
p = pattern.finditer('hai hello bro hello')
print(p)
print(next(p))
print(next(p))