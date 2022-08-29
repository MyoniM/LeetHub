class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(path, summ, candidates):
            if summ > target:
                return
            if summ == target:
                res.append(path)
                return
            for i in range(len(candidates)):
                if i==0 or candidates[i-1] != candidates[i]:
                    dfs(path+[candidates[i]], summ+candidates[i], candidates[i+1:])
        
        candidates.sort()    
        dfs([], 0, candidates)
        return res