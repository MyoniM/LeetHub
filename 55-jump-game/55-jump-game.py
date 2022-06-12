class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        l = len(nums)
        g = l - 1
        for i in reversed(range(l - 1)):
            if nums[i] + i >= g:
                g = i
        return g == 0
                