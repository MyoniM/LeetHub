class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        leftMostProd = nums[0] * nums[1]
        rightMostProd = nums[-2] * nums[-3]
        
        return max(nums[-1] * leftMostProd, nums[-1] * rightMostProd)
        