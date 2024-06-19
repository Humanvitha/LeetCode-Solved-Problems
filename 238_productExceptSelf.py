class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [None] * n
        result[0] = 1
        lp = 1 #left product
        for i in range(1,n):
            lp = lp * nums[i-1]
            result[i] = lp
        rp = 1 #right product
        for i in range(n-2,-1,-1):
            rp = rp * nums[i+1]
            result[i] = result[i] * rp
        return result

# Time complexity O(2n)
# Space complexity O(n)


# Problem 238: https://leetcode.com/problems/product-of-array-except-self/description/