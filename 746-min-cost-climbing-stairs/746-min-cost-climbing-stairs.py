class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        vis = {}
        return min(self.minClimb(cost, vis, 0), self.minClimb(cost, vis, 1))
    
    def minClimb(self, cost, vis, step):
        if step in vis: return vis[step]
        if step >= len(cost): return 0
        if step == len(cost) - 1: return cost[step]
        
        minCost = float('inf')
        for s in [1,2]:
            minCost = min(minCost, self.minClimb(cost, vis, step + s))
        
        vis[step] = minCost + cost[step]
        return vis[step]
        
        