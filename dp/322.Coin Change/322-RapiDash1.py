class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        
        if amount == 0:
            return 0
        
        minCoinsArray = [float("inf")]*(amount+1)
        minCoinsArray[0] = 0
        for coin in coins:
            if coin > amount:
                break
                
            minCoinsArray[coin] = 1
        
        for coinValue in range(1, amount+1):
            for reducibleCoin in coins:
                if reducibleCoin > coinValue:
                    break
                    
                minCoinsArray[coinValue] = min(minCoinsArray[coinValue], 1+minCoinsArray[coinValue - reducibleCoin])
                
        return minCoinsArray[-1] if minCoinsArray[-1] != float("inf") else -1
            

# Time Complexity: O(amount*len(coins))
# Space Complexity: O(amount)