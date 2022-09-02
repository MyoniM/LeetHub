class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        p = []
        
        def isP(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
    
        def dfs(i):
            if i == len(s):
                res.append(p.copy())
                return 
            
            for idx in range(i, len(s)):
                if isP(s, i, idx):
                    p.append(s[i: idx + 1])
                    dfs(idx + 1)
                    p.pop()
                    
        dfs(0)
        return res