class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = dict()
        hashMap[0] = 1
        runningSum = 0
        count = 0
        for i in range(len(nums)):
            runningSum += nums[i]
            complement = runningSum - k
            if complement in hashMap.keys():
                count += hashMap[complement]
            if runningSum not in hashMap.keys():
                hashMap[runningSum] = 1
            else:
                hashMap[runningSum] += 1
        return count

# Problem 506: https://leetcode.com/problems/subarray-sum-equals-k/description/