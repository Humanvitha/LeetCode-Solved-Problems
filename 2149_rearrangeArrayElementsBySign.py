class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = 0
        negative = 1
        result = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                result[positive] = nums[i]
                positive += 2
            else:
                result[negative] = nums[i]
                negative += 2
        return result
    
# Problem 2149: https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
# Time Complexity O(n)
# Space Complexity O(n)