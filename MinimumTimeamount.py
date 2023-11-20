#Minimum Amount of Time to Collect Garbage
garbage = ["MMM","PGM","GP"]
travel = [3,10]
i=0
minute = 0
index = None
l=['M','P','G']
print(garbage)
while i < len(garbage):
    if l[-1] in garbage[i]:
        c = garbage[i].count(l[-1])
        minute += c
        index = i
        
    i += 1
    if i == len(garbage):
        i = 0
        if index is not None:
            minute += sum(travel[:index])
            index = None
        l.pop()
    if l == []:
        break
print(minute)