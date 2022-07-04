class Solution:
#   TOP-DOWN WITH MEMOIZATION
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         visited = {}
#         minUsedCoins = self.getUsedCoins(amount, coins, visited)
#         return minUsedCoins if minUsedCoins is not None else -1
            
#     def getUsedCoins(self, amount, coins, visited):
#         if amount == 0: return 0
#         if amount < 0: return None
#         if amount in visited: return visited[amount]
        
#         minCount = None
#         for coin in coins:
#             newAmount = amount - coin
#             usedCoins = self.getUsedCoins(newAmount, coins, visited)
#             if usedCoins is not None:
#                 usedCoins += 1
#                 if minCount is None or usedCoins < minCount:  
#                     minCount = usedCoins
                    
#         visited[amount] = minCount
#         return minCount
    
#   BOTTOM-UP WITH TABULATION
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [-1] * (amount + 1)
        table[0] = 0
        
        for i in range(len(table)):
            if table[i] == -1: continue
            for coin in coins:
                idxToUpdate = coin + i
                if idxToUpdate >= len(table): continue
                if table[idxToUpdate] == -1:
                    table[idxToUpdate] = table[i] + 1
                else:
                    table[idxToUpdate] = min(table[idxToUpdate], table[i] + 1)
                    
        return table[amount]
        
        
        
        
        