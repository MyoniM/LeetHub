class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        m = 0
        for e in nums:
            if e - 1 not in seq:
                c = 1
                while e + 1 in seq:
                    c += 1
                    e += 1
                m = max(m, c)    
        return m
    
    