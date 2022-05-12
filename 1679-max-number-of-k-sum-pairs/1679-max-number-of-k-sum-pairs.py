class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        if len(nums) == 1: return 0
        nums.sort()
        max_op, left, right = 0,0, len(nums) - 1
        
        while left < right:
            sum_res = nums[left] + nums[right]
            if sum_res == k:
                left+=1
                right-=1
                max_op+=1

            elif sum_res < k: left+=1
            else: right-=1
        
        return max_op
        