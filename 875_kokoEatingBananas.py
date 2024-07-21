class Solution:
    def calculateTime(self, piles: List[int], currentVal: int) -> int:
        hours = 0
        for pile in piles:
            hours += (pile + currentVal - 1) // currentVal
        return hours
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            currentVal = low + (high - low) // 2
            if self.calculateTime(piles, currentVal) <= h:
                high = currentVal
            else:
                low = currentVal + 1
        
        return low

# Time Complexity O(log(max(piles)) * h)
# Space Complexity O(1)
# Problem 875: https://leetcode.com/problems/koko-eating-bananas/