class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left , right = 0, len(nums) - 1
        
        while left <= right:
            center_index = left + (right - left) // 2
            if nums[center_index] == target: return center_index
            elif nums[center_index] < target: left = center_index +1
            else: right = center_index -1
            
        return -1