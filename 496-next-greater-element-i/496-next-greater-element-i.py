class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash2 = {}
        r = []
        for i in range(len(nums2)):
            hash2[nums2[i]] = i
            
        for e in nums1:
            i2 = hash2[e]
            r.append(self.getNextMax(i2, nums2))
        return r
    
    def getNextMax(self, ii, arr):
        n = -1
        for i in range(ii, len(arr)):
            if arr[i] > arr[ii]:
                n = arr[i]
                break
        return n