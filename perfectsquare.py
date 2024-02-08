class Solution:
    def numSquares(self, n: int) -> int:
    # generate perfect squares <= n
        perfect_squares = [x**2 for x in range(1, int(sqrt(n))+1)]
        
        # problem reduces to coin change, with coin values of perfect_squares
        dp = [n for _ in range(n+1)]   # res[i] is the least #pf_sq for n = i
        dp[0] = 0
        for i in range(1, n+1):
            for square in perfect_squares:
                if i - square >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - square])

        return dp[n]
            