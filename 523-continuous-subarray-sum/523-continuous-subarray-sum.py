class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if l < 2: return False
        
        h = {0:-1}
        p = 0
        for i in range(l):
            p += nums[i]
            r = p % k
            if r not in h: h[r] = i
            else: 
                if i - h[r] > 1: return True 
        return False