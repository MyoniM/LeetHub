class Solution:
    def findMin(self, n: List[int]) -> int:
        l, r = 0, len(n) - 1
        mn = math.inf
        while l <= r:
            m = (l + r) // 2
            mn = min(n[m], mn)
            if n[m] < n[r]: r = m - 1
            else: l = m + 1

        return mn