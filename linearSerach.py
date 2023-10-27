#WAP for linear Search
def linearSearch(l,t):
    for i in l:
        if i==t:
            return True
    else:
        return False
l=[2,9,11,90,34,7,22,39]
target=int(input())
print("found") if linearSearch(l,target) else print("Not found")