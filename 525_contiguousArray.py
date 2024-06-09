class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashMap = dict()
        hashMap[0] = -1
        runningSum = 0
        maxLength = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                runningSum -= 1
            else:
                runningSum += 1
            if runningSum in hashMap.keys():
                if i - hashMap[runningSum] > maxLength:
                    maxLength = i - hashMap[runningSum]
            else:
                hashMap[runningSum] = i
        return maxLength

# Problem 525: https://leetcode.com/problems/contiguous-array/description/