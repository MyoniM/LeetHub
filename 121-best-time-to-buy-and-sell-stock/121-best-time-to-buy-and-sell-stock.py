class Solution:
    def maxProfit(self, p: List[int]) -> int:
        mx = 0
        l, r = 0, 1
        while r < len(p):
            if p[r] <= p[l]: l = r
            else: mx = max(mx, p[r] - p[l])
            r += 1
        return mx