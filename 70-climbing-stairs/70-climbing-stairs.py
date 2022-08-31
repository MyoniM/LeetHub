class Solution:
    def climbStairs(self, n: int) -> int:
        vis = {}
        return self.climb(0, n, vis)
    
    def climb(self, step, n, vis):
        if step > n: return 0
        if step in vis: return vis[step]
        if step == n: return 1
        
        reachCont = 0
        reachCont += self.climb(step + 1, n, vis)
        reachCont += self.climb(step + 2, n, vis)
        vis[step] = reachCont
        
        return vis[step]
        
        