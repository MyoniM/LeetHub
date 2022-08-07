class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            m = (l + r) // 2
            s = self.sumByDivisor(m, nums)
            if s > threshold:
                l = m + 1
            else:
                r = m - 1
        return l
    
    def sumByDivisor(self, num, nums):
        total = 0
        for n in nums:
            total += ceil(n/num)
        return total