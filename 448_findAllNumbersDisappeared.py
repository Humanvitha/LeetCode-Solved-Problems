class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result
    
# Time complexity O(n)
# Space complexity O(1) output is not considered as a separate space
# Problem 448: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/