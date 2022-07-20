class Solution:
    def jump(self, nums: List[int]) -> int:
#         return self.helper(0, nums, {})
    
#     def helper(self, idx, nums, memo):
#         if idx >= len(nums) - 1: return 0
#         if idx in memo: return memo[idx]
        
#         minJump = math.inf
#         for jp in range(1, nums[idx] + 1):
#             minJump = min(minJump, self.helper(idx + jp, nums, memo))
#         memo[idx] = minJump + 1
#         return minJump + 1

        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res