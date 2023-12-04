#Largest 3-Same-Digit Number in String
num = "2300019"
large = ''
for i in range(len(num)-2):
    if num[i:i+3] > large and num[i:i+3] == num[i]*3:
        large = num[i:i+3]
print(large)