#climbing Stairs
def climbStairs(n):
    if n <= 2:
        return n
    dp1 = 1
    dp2 = 2
    res = 0
    for i in range(2,n):
        res = dp1+dp2
        dp1,dp2 = dp2,res
    return res
print(climbStairs(4))