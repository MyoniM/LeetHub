class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solveSudokuPartial(0, 0, board)
        return board

    def solveSudokuPartial(self, row, col, board):
        currentRow = row
        currentCol = col
        if currentCol == 9:
            currentRow += 1
            currentCol = 0
            if currentRow == 9:
                return True

        if board[currentRow][currentCol] == ".":
            return self.trySolvingWithGuess(currentRow, currentCol, board)
        return self.solveSudokuPartial(currentRow, currentCol + 1, board)

    def trySolvingWithGuess(self, row, col, board):
        for num in range(1, 10):
            if self.isValidPosition(str(num), row, col, board):
                board[row][col] = str(num)
                if self.solveSudokuPartial(row, col + 1, board):
                    return True
        board[row][col] = "."
        return False

    def isValidPosition(self, value, row, col, board):
        isValidRow = value not in board[row]
        isValidColumn = value not in map(lambda r: r[col], board)

        if not isValidRow or not isValidColumn: return False

        rowPartitionStartIdx = (row // 3) * 3
        colPartitionStartIdx = (col // 3) * 3

        for r in range(3):
            for c in range(3):
                rowToCheck = rowPartitionStartIdx + r
                colToCheck = colPartitionStartIdx + c
                if board[rowToCheck][colToCheck] == value: return False
        return True

