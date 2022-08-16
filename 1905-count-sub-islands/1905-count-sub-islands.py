class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows,cols = len(grid1), len(grid1[0])
        
        visited = set()
        subIslands = 0
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid2[r][c] != 1:
                return True
            if grid1[r][c] != 1: return False
            visited.add((r,c))
            direction =  [[1,0],[-1,0],[0,-1],[0,1]]
            flag = True
            for dr, dc in direction:
                if dfs(r+ dr, c + dc) == False:
                    flag = False 
            return flag
            
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and (i, j) not in visited and dfs(i, j) == True:
                    subIslands += 1
        return subIslands