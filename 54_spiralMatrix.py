class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        left = top = 0
        right = n - 1
        bottom = m - 1
        while left <= right and top <= bottom:
            # top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            # right column
            if left <= right and top <= bottom:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
            right -= 1
            # bottom row
            if left <= right and top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
            bottom -= 1
            # left column
            if left <= right and top <= bottom:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
            left += 1
        return result

# Time complexity O(sizeofmatrix)
# Space complexity O(sizeofmatrix)
# Problem 54: https://leetcode.com/problems/spiral-matrix/description/