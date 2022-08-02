class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                minValue = float("inf")
                if i-1 >= 0:
                    minValue = min(minValue, grid[i-1][j])
                if j-1 >= 0:
                    minValue = min(minValue, grid[i][j-1])
                
                grid[i][j] += (minValue if minValue != float("inf") else 0)
                
        return grid[-1][-1]
        
# Time Complexity: O(n)
# Space Complexity: O(1)
# Here n is number of elements in the matrix