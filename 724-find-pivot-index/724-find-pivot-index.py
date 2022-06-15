class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        pSum = [nums[0]]
        for n in nums[1:]:
            pSum.append(pSum[-1] + n)
        
        for i, e in enumerate(pSum):
            if pSum[-1] - e == left:
                return i
            left = e
        return -1