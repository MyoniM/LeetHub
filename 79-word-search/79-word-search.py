class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        L = len(word)
        RB = len(board)
        CB = len(board[0])
        for row in range(RB):
            for col in range(CB):
                if self.find(row, col, 0, RB, CB, L, word, board):
                    return True
        return False
        
    def find(self, row, col, letterIdx, RB, CB, L, word, board):        
        if letterIdx == L:
            return True

        if row < 0 or col < 0 or row >= RB or col >= CB: 
            return False
        
        if board[row][col] != word[letterIdx]:
            return False
        
        DIRECTIONS = [[0,1], [0,-1], [1,0], [-1,0]]
        temp = board[row][col]
        board[row][col] = "#"
        for nRow, nCol in DIRECTIONS:
            if self.find(row + nRow, col + nCol, letterIdx + 1, RB, CB, L, word, board):
                return True
        board[row][col] = temp    

    
    
    
            
            
            