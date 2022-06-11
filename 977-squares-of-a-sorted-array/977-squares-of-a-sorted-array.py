class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        
        index = right = len(nums) - 1
        left = 0
         
        while left <= right:
            leftSquared = nums[left]**2
            rightSuared = nums[right]**2
            if leftSquared > rightSuared:
                result[index] = leftSquared
                left += 1
            else:
                result[index] = rightSuared
                right -= 1
            index -= 1
        return result