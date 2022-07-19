class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    cellIsValid = self.validateCell(r, c, board)
                    if not cellIsValid: return False
        return True
    
    def validateCell(self, row, col, board):
        val = board[row][col]
        
        isValidRow = self.checkRow(val, row, col, board)
        isValidColumn = self.checkCol(val, row, col, board)
        if not isValidRow or not isValidColumn: return False
        
        partialRowStart = (row // 3) * 3
        partialColStart = (col // 3) * 3 

        for r in range(3):
            for c in range(3):
                currentRow = partialRowStart + r
                currentCol = partialColStart + c
                notCurrentCell = currentRow != row and currentCol != col
                if notCurrentCell and board[currentRow][currentCol] == val:
                    return False
        return True
    
    def checkRow(self, val, row, col, board):
        for i, e in enumerate(board[row]):
            if i != col and e == val: return False
        return True
    
    def checkCol(self, val, row, col, board):
        colVals = map(lambda r: r[col], board)
        for i, e in enumerate(colVals):
            if i != row and e == val: return False
        return True