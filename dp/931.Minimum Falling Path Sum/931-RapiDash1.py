class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        for i in range(len(matrix)-2, -1, -1):
            for j in range(len(matrix[0])-1, -1, -1):
                minValue = matrix[i+1][j]
                if j > 0:
                    minValue = min(minValue, matrix[i+1][j-1])
                if j < len(matrix[0])-1:
                    minValue = min(minValue, matrix[i+1][j+1])
                    
                matrix[i][j] += minValue
                
        return min(matrix[0])
                    

# Time Complexity: O(n)
# Space Complexity: O(1)
# Here n is the number of elements in the matrix