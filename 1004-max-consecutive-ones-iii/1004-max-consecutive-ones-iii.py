class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = res = 0
        while r < len(nums):
            if nums[r] == 0: k -= 1
            while k < 0:
                if nums[l] == 0: k += 1
                l += 1
            r += 1
            res = max(r - l, res)
        return res