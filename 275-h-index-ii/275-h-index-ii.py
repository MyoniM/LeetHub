class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        while l <= r :
            m = (l + r) // 2
            if m + citations[m] >= n:
                r = m - 1
            else:
                l = m + 1
        return n - l