class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # left = 0
#         for i, n in enumerate(nums):
#             if i == 0: continue
#             nums[i] = nums[i - 1] + n
        
#         for i, e in enumerate(nums):
#             if nums[-1] - e == left:
#                 return i
#             left = e
#         return -1
        left = 0
        s = sum(nums)
        pSum = 0
        for i, e in enumerate(nums):
            pSum += e
            if s - pSum == left:
                return i
            left = pSum
        return -1