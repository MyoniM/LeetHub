class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
#         v = {}
#         c = self.helper(0, nums, k, v)
#         print(v)
#     def helper(self, currIdx, nums, k, v):
#         numsLen = len(nums)
#         if currIdx == numsLen - 1: return nums[currIdx]
#         key = "{}-{}".format(currIdx, nums[currIdx])
#         if key in v:
#             print(key)
#             return v[key]
#         endIdx = min(numsLen, currIdx + k + 1)
        
#         maxSum = -math.inf
#         for i in range(currIdx + 1, endIdx):
#             result = self.helper(i, nums, k, v)
#             maxSum = max(maxSum, result)
#         v[key] = nums[currIdx] + maxSum
#         return nums[currIdx] + maxSum

        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        q=deque([(dp[0],0)])
        for i in range(1,n):
            dp[i]=q[0][0]+nums[i]
            while q and dp[i]>q[-1][0]:
                q.pop()
            q.append((dp[i],i))
            if q[0][1]<=i-k:
                q.popleft()
        return dp[n-1]