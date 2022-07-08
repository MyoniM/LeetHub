class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        stack = []
        num1_hash = {e:i for i,e in enumerate(nums1)}

        for e in nums2:
            while stack and stack[-1] < e:
                ans[num1_hash[stack.pop()]] = e

            if e in num1_hash: stack.append(e)

        return ans 
