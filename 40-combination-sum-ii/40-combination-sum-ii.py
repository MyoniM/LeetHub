class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(path, summ, k):
            if summ > target:
                return
            if summ == target:
                res.append(path)
                return
            for i in range(k, len(candidates)):
                if i==k or candidates[i-1] != candidates[i]:
                    dfs(path+[candidates[i]], summ+candidates[i], i+1)
        
        candidates.sort()    
        dfs([], 0, 0)
        return res