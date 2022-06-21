class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Best and average O(n) time | O(1) space
        # Worst O(n^2) time | O(1) space
        position = len(nums) - k
        return self.quickSelectHelper(nums, 0, len(nums) - 1, position)
    
    def quickSelectHelper(self, array, startIdx, endIdx, position):
        while True:
            pivot = startIdx
            left = startIdx + 1
            right = endIdx
            
            while left <= right:
                if array[left] > array[pivot] and array[right] < array[pivot]:
                    self.swap(left, right, array)
                if array[left] <= array[pivot]:
                    left += 1
                if array[right] >= array[pivot]:
                    right -= 1
            self.swap(right, pivot, array)
            if right == position:
                return array[right]
            elif right < position:
                startIdx = right + 1
            else:
                endIdx = right - 1
                    
    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]