class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        s = [0]
        p = [0]
        for n in nums:
            p.append(p[-1] + n)
            
        for n in reversed(nums):
            s.append(s[-1] + n)
        print(p, s)
        for i in range(l):
            if p[i] == s[l-1-i]: return i
        return -1