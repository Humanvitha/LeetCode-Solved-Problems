class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            #reached a range which is sorted in unsorted array
            if nums[low] <= nums[high]:
                return nums[low]
            mid = low + (high - low) // 2
            if (mid != 0 and nums[mid - 1] >= nums[mid]) and (mid != n-1 and nums[mid] <= nums[mid + 1]):
                return nums[mid]
            elif nums[low] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# Problem 153: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/