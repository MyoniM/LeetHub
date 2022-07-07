class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        c = 0
        l, r = 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                c += 1
                l += 1
                r -= 1
            elif s < k:
                l += 1
            else:
                r -= 1
        return c
        