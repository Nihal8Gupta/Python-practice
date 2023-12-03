#Minimum Time Visiting All Points
points = [[1,1],[3,4],[-1,0]]
i = 0
count = 0
while i < len(points)-1:
    if points[i][0] < points[i+1][0]:
        points[i][0] += 1
        flag = True
    if points[i][1] < points[i+1][1]:
        points[i][1] += 1
        flag = True
    if points[i][0] > points[i+1][0]:
        points[i][0] -= 1
        flag = True
    if points[i][1] > points[i+1][1]:
        points[i][1] -= 1
        flag = True
    if points[i][0] == points[i+1][0] and points[i][1] == points[i+1][1]:
        i += 1
    if flag:
        count += 1
        flag = False

print(points,count)