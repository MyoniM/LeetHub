class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi, res = values[0], 0
        for i in range(1, len(values)):
            res = max(res, maxi + values[i] - i)
            maxi = max(maxi, values[i] + i)
        return res