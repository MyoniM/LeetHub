class Solution:
#   TOP-DOWN WITH MEMOIZATION
    def coinChange(self, coins: List[int], amount: int) -> int:
        visited = {}
        minUsedCoinsArray = self.getUsedCoins(amount, coins, visited)
        return minUsedCoinsArray if minUsedCoinsArray is not None else -1
            
    def getUsedCoins(self, amount, coins, visited):
        if amount == 0: return 0
        if amount < 0: return None
        if amount in visited: return visited[amount]
        
        minCountArray = None
        for coin in coins:
            newAmount = amount - coin
            usedCoins = self.getUsedCoins(newAmount, coins, visited)
            if usedCoins is not None:
                if minCountArray is None or usedCoins + 1 < minCountArray:  
                    minCountArray = usedCoins + 1
                    
        visited[amount] = minCountArray
        return minCountArray
    
#   BOTTOM-UP WITH TABULATION
    # def coinChange(self, coins: List[int], amount: int) -> int:
        