class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                left = mid
                right = mid
                while left - 1 >= 0 and nums[left] == nums[left - 1]:
                    left -= 1
                while right + 1 < len(nums) and nums[right] == nums[right + 1]:
                    right += 1
                return [left, right]
                    
        return [-1, -1]