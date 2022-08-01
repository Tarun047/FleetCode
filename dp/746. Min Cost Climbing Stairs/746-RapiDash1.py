class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        i = 2
        while i < len(cost):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            i += 1
        
        return min(dp[-1], dp[-2])
        

# Time Complexity: O(n)
# Space Complexity: O(n)