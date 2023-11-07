dist = [1,3,4]
speed = [1,1,1]
dist = [3,2,4]
speed = [5,3,2]
l=len(dist)
time=sorted(list(map(lambda i:dist[i]/speed[i],range(l))))
print(time)
count=0
for i in range(l):
    if time[i]>0:
        count+=1
    else:
        break
    time=list(map(lambda i:time[i]-1,range(l)))
print(count)