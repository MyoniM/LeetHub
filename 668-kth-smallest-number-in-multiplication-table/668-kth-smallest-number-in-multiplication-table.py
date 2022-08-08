class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def enough(x):
            res = 0
            for i in range(1, m + 1):
                res += min(x // i, n)
            return res
        
        l, r = 1, m * n
        while l <= r:
            mid = (l + r) // 2
            curr = enough(mid)
            print(mid, curr)
            if curr < k:
                l = mid + 1
            else:
                r = mid - 1
        return l