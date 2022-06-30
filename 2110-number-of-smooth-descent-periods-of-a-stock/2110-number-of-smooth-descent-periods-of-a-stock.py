class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l = ans = 0
        for r in range(1, len(prices)):
            if prices[r - 1] - prices[r] == 1:
                ans += r - l
            else:
                l = r
        return ans + len(prices)