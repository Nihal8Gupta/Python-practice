#5 15 45
def energyProduced(initialE,rate,second): #5 3 3
    nl=[initialE]
    for i in range(1,second):
        nl.append(nl[i-1]*rate)
    nl=[str(i) for i in nl]
    return ' '.join(nl)

r=energyProduced(5,3,3)
print(r)