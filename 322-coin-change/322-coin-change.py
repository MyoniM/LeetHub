class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        visited = {}
        minUsedCoiunesArray = self.getUsedCoins(amount, coins, visited)
        return len(minUsedCoiunesArray) if minUsedCoiunesArray is not None else -1
            
    def getUsedCoins(self, amount, coins, visited):
        if amount == 0: return []
        if amount < 0: return None
        if amount in visited: return visited[amount]
        
        minCountArray = None
        for coin in coins:
            newAmount = amount - coin
            usedCoins = self.getUsedCoins(newAmount, coins, visited)
            if usedCoins is not None:
                minCombination = usedCoins + [coin]
                if minCountArray is None or len(minCombination) < len(minCountArray):  
                    minCountArray = minCombination
                    
        visited[amount] = minCountArray
        return minCountArray
    