class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        leastPerfectSquares = [i for i in range(n+1)]
        
        i = 1
        squares = []
        while i**2 <= n:
            squares.append(i**2)
            leastPerfectSquares[i**2] = 1
            i += 1
            
        
        for i in range(n+1):
            for square in squares:
                if square <= i:
                    leastPerfectSquares[i] = min(leastPerfectSquares[i], leastPerfectSquares[square] + leastPerfectSquares[i-square])
                else:
                    break
        
        return leastPerfectSquares[-1]
        

# Time Complexity: O(n*len(squares))
# Space Complexity: O(n)
        