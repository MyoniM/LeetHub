class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def swap(i, j, arr):
            arr[i], arr[j] = arr[j], arr[i]
        
        def dfs(j):
            if j == len(nums) - 1: 
                res.append(nums.copy())
                return
            
            for i in range(j, len(nums)):
                swap(i, j, nums)
                dfs(j+1)
                swap(i, j, nums)
                
        dfs(0)
        return res
        