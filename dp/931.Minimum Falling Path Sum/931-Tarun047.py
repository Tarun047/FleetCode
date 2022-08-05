class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ans = float('inf')
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                if i > 0:
                    cell_value = matrix[i - 1][j] + matrix[i][j]
                    if j > 0:
                        cell_value = min(cell_value, matrix[i - 1][j - 1] + matrix[i][j])
                    if j < len(matrix[0]) - 1:
                        cell_value = min(cell_value, matrix[i - 1][j + 1] + matrix[i][j])
                    matrix[i][j] = cell_value
                if i == len(matrix) - 1:
                    ans = min(ans, matrix[i][j])
        return ans
