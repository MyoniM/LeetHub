class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        s = sum(nums)
        pSum = 0
        for i, e in enumerate(nums):
            pSum += e
            if s - pSum == left:
                return i
            left = pSum
        return -1