class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = res = 0
        # nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
        # nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        while r < len(nums):
            if nums[r] == 0: k -= 1
            while k < 0:
                if nums[l] == 0: k += 1
                l += 1
            r += 1
            res = max(r - l, res)
        return res