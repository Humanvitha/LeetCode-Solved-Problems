class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1
        while low <= high:
            mid = low + (high - low) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                high = mid - 1
            else:
                low = mid + 1
        return False

# Problem 74: https://leetcode.com/problems/search-a-2d-matrix/description/