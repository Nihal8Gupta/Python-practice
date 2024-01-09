#WAP to validate hexadecimal color RGB
import re
pattern =re.compile(r'#[0-9a-fA-F]{3,6}')
print(pattern.match('#FFF19a'))