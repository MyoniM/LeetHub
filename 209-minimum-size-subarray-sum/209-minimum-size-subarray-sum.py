class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sL = n + 1
        
        s = l = r = 0

        while r < n:
            s += nums[r]
            while s >= target:
                sL = min(sL, r - l + 1)
                s -= nums[l]
                l += 1
            r += 1
        return sL if sL < n + 1 else 0 