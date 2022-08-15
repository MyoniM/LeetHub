class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        def dfs(board, r, c):
            if r<0 or c<0 or r==m or c==n or board[r][c] != "E":
                return 0
            adjacent = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,1],[-1,1],[1,-1]]
            mines = 0
            for ar, ac in adjacent:
                row, col = ar+r, ac+c
                if row in range(0,m) and col in range(0,n) and board[row][col] == "M":
                    mines += 1
            board[r][c] = str(mines) if mines else "B"
            
            if mines:
                return 0
                
            for ar, ac in adjacent:
                dfs(board, ar+r, ac+c)
            
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        dfs(board, click[0], click[1])
        return board