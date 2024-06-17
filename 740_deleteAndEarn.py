class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums)
        countArray = [0] * (n+1)
        for i in nums:
            countArray[i] += i
        dp = [0] * (n + 1)
        dp[1] = countArray[1]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+countArray[i])
        return dp[-1]
# Problem 740: https://leetcode.com/problems/delete-and-earn/description/