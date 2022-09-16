class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        prev = ""
        for i, n in enumerate(nums):
            if prev == n: continue
            nums[idx], nums[i] = nums[i], nums[idx]
            prev = n
            idx += 1        
        return idx