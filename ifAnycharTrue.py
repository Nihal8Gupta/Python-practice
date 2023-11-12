#Check if any is True
s = input()
al_num=False
al=False
dig=False
low=False
upp=False
for i in s:
    al_num = al_num or i.isalnum() 
    al  = al or i.isalpha()
    dig = dig or i.isdigit()
    low = low or i.islower()
    upp = upp or i.isupper()
print(al_num)
print(al)
print(dig)
print(low)
print(upp)