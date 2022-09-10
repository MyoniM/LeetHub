class Solution:
    def uniquePaths(self, h: int, w: int) -> int:
        grid = [ ([0] * (w + 1)) for _ in range(h+1)]
        grid[1][1] = 1
        for r in range(h + 1): 
            for c in range(w + 1): 
                curr = grid[r][c]
                if r < h: grid[r+1][c] += curr
                if c < w: grid[r][c+1] += curr
        return grid[h][w]