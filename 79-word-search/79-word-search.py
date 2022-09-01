class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c, ind):
            if r < 0 or c < 0 or r == row or c == col:
                return False
            if board[r][c] != word[ind]:
                return False
            if ind == len(word)-1:
                return True
            tmp = board[r][c]
            board[r][c] = "0"
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if dfs(nr, nc, ind+1):
                    return True
            board[r][c] = tmp
            return False
        
        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False

    
    
    
            
            
            