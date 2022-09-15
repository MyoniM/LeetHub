class Solution:
    count = 0
    def closedIsland(self, grid: List[List[int]]) -> int:
        vis = set()
        def getNeigh(r, c):
            neigh = []
            D = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in D:
                neigh.append((r+dr, c+dc))
            return neigh
        
        def dfs(r, c):
            if r < 0 or r >= len(grid): return 
            if c < 0 or c >= len(grid[r]): return
            if grid[r][c] == 1: return
            if (r, c) in vis: return
            vis.add((r,c))
            for nr, nc in getNeigh(r, c):
                dfs(nr, nc)
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if r in (0, len(grid)-1) or c in (0, len(grid[0])-1):
                    dfs(r, c)
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0 and (r, c) not in vis:
                    dfs(r, c)
                    self.count += 1
        return self.count
