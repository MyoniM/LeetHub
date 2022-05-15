class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        
        left  = 0
        right = len(nums) - 1
        
        max_pair_sum = 0
        
        while left < right:
            max_pair_sum = max(nums[left] + nums[right], max_pair_sum)
            
            left+=1
            right-=1
            
        return max_pair_sum