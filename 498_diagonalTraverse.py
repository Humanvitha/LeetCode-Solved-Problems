class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        result = [0] * (m * n)
        direction = True  # indicates upward direction
        i = j = 0
        for k in range(m*n):
            result[k] = mat[i][j]
            if direction:
                if i == 0 and j == n - 1:
                    direction = False
                    i += 1
                elif j == n - 1:
                    direction = False
                    i += 1
                elif i == 0:
                    direction = False
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == m - 1 and j == 0:
                    direction = True
                    j += 1
                elif j == 0:
                    direction = True
                    i += 1
                elif i == m - 1:
                    direction = True
                    j += 1
                else:
                    i += 1
                    j -= 1
        return result

# Time complexity O(sizeofmatrix)
# Space complexity O(sizeofmatrix)
# Problem 498: https://leetcode.com/problems/diagonal-traverse/description/