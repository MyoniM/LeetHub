class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time intesive sln, O(n^2) time worst case | O(1) space
        k = k % len(nums)
        # while k:
        #     k -= 1
        #     last = nums.pop(-1)
        #     nums.insert(0, last)
        
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
        l, r = 0, k - 1
        while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
               
        
        
            