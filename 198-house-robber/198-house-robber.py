class Solution:
    def rob(self, nums: List[int]) -> int:
        b = s = 0
        for m in nums:
            if (m + s) > b:
                t = s
                s = b
                b = m + t
                continue
            s = b
        return b