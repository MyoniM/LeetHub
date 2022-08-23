class Solution:
    islandsCount = 0
    DIRECTIONS = [[-1,0], [1,0], [0,-1], [0,1]]
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for r in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if self.bfs(r, c, grid, visited): self.islandsCount += 1
        return self.islandsCount
                    
    def bfs(self, r, c, grid, visited):
        if r < 0 or r == len(grid): return False
        if c < 0 or c == len(grid[0]): return False
        if visited[r][c]: return False
        if grid[r][c] == "0": return 0
        visited[r][c] = True
        for dr, dc in self.DIRECTIONS:
            self.bfs(r + dr, c + dc, grid, visited)
        return True