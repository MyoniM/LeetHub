class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(path, arr):
            if not arr:
                res.append(path)
            for i in range(len(arr)):
                if i==0 or arr[i-1] != arr[i]: 
                    dfs(path + [arr[i]], arr[:i] + arr[i+1:])
        
        nums.sort()
        dfs([], nums)
        return res