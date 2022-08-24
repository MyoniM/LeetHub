class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [[1,0],[-1,0],[0,1],[0,-1]]
        pac, atl = set(), set()
        
        def dfs(r, c, visited, prevHeight):
            if r < 0 or c < 0 or r == len(heights) or c == len(heights[0]) or (r, c) in visited or prevHeight > heights[r][c]: return
            visited.add((r, c))
            for dr, dc in DIRECTIONS:
                dfs(r+dr, c+dc, visited, heights[r][c])
            
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            
        for c in range(COLS):
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
            
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            
        for r in range(ROWS):
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res