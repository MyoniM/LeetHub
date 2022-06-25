class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = nums[0]
        currentMax = nums[0]
        for num in nums[1:]:
            currentMax = max(currentMax + num, num)
            maxSoFar = max(currentMax, maxSoFar)
        return maxSoFar