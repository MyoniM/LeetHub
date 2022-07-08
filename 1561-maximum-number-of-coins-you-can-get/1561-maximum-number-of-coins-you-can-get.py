class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        maxCoinNum = 0
        for i in range(n // 3):
            startFromBackIdx = n - 1 - (i * 2)
            maxCoinNum += piles[startFromBackIdx - 1]
        return maxCoinNum
