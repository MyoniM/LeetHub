class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        
        if n > m: return self.findMedianSortedArrays(nums2,nums1)

        low = 0
        high = n

        while low <= high:
            x_mid = (low+high)//2
            y_mid = (n+m+1)//2 - x_mid


            maxLeftx = nums1[x_mid -1] if x_mid != 0 else -99999999
            minRightx = nums1[x_mid] if x_mid != n else 99999999

            maxLefty = nums2[y_mid -1] if y_mid != 0 else -99999999
            minRighty = nums2[y_mid] if y_mid != m else 99999999

            if (maxLeftx <= minRighty and maxLefty <= minRightx):
                # correct partition place
                # now check if the array has an even/odd length
                if (n + m) % 2 == 0:
                    # array has even length
                    return (max(maxLeftx,maxLefty) + min(minRightx, minRighty))/2
                else:
                    # array has an odd length
                    return max(maxLeftx,maxLefty)
            elif maxLeftx > minRighty: high = x_mid - 1
            else: low = x_mid + 1


    