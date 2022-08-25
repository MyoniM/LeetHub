class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def dfs(path, summ, k):
            if summ > target:
                return
            if summ == target:
                res.append(path)
                return
                
            for i in range(k,n):
                dfs(path+[candidates[i]], summ+candidates[i], i)
        
        dfs([], 0, 0)
        return res