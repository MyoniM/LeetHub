class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        visited = {}
        minUsedCoinsArray = self.getUsedCoins(amount, coins, visited)
        return len(minUsedCoinsArray) if minUsedCoinsArray is not None else -1
            
    def getUsedCoins(self, amount, coins, visited):
        if amount == 0: return []
        if amount < 0: return None
        if amount in visited: return visited[amount]
        
        minCountArray = None
        for coin in coins:
            newAmount = amount - coin
            usedCoins = self.getUsedCoins(newAmount, coins, visited)
            if usedCoins is not None:
                if minCountArray is None or len(usedCoins) + 1 < len(minCountArray):  
                    minCountArray = usedCoins + [coin]
                    
        visited[amount] = minCountArray
        return minCountArray
    