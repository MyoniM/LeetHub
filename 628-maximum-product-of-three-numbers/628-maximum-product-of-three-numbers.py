class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        leftMostProd = nums[0] * nums[1]
        rightMostProd = nums[-2] * nums[-3]
        
        leftIsBig = leftMostProd > rightMostProd
        endIsPositive = nums[-1] > 0
        
        if endIsPositive:
            return nums[-1] * leftMostProd if leftIsBig else nums[-1] * rightMostProd
        else:
            return nums[-1] * rightMostProd if leftIsBig else nums[-1] * leftMostProd
