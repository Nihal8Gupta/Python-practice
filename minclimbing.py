#WAP min cost climb
cost=[1,100,1,1,1,100,1,1,100,1]
cost.append(0)
print(cost)
l=len(cost)
for i in range(l-3,-1,-1):
    cost[i]+=min(cost[i+1],cost[i+2]) 
print(min(cost[0],cost[1]))