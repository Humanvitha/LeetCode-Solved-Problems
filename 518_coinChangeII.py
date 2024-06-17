class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        n = amount
        dp = [[None]*(n+1)]*(m+1)
        
        for i in range(n+1):
            dp[0][i] = 0
        dp[0][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-coins[i-1]]
        return dp[-1][-1]
# Problem 518: https://leetcode.com/problems/coin-change-ii/description/