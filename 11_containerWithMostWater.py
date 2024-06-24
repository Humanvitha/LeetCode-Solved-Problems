class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(height) - 1
        maxArea = 0
        while leftPointer < rightPointer:
            area = min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer)
            if area > maxArea:
                maxArea = area
            if height[leftPointer] < height[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -= 1
        return maxArea
# time complexity O(n)  
# Problem 11: https://leetcode.com/problems/container-with-most-water/description/