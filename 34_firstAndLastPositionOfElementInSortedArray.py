class Solution:
    def binarySearchLeft(self, nums: List[int], low: int, high: int, target: int) -> int:
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] ==  target:
                if mid == 0 or nums[mid - 1] < nums[mid]:
                    return mid
                else :
                    high = mid - 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    def binarySearchRight(self, nums: List[int], low: int, high: int, target: int) -> int:
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] ==  target:
                if mid == len(nums) - 1 or nums[mid] < nums[mid + 1]:
                    return mid
                else :
                    low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearchLeft(nums, 0, len(nums) - 1, target)
        if left == -1:
            return [-1, -1]
        right = self.binarySearchRight(nums, left, len(nums) - 1, target)
        return [left, right]

# Problem 34: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/