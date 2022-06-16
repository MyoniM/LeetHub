class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixSum = self.getPrefixSum(matrix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        ps = self.prefixSum
        for i in range(row2 + 1 - row1):
            sub = 0 if col1 == 0 else ps[row1 + i][col1 - 1]
            s += ps[row1 + i][col2] - sub
        return s
    
    def getPrefixSum(self, matrix):
        prefixSum = []
        for r in range(len(matrix)):
            prefixSum.append([matrix[r][0]])
            for c in range(len(matrix[r])):
                if c == 0: continue 
                prefixSum[r].append(prefixSum[r][-1] + matrix[r][c])
        return prefixSum
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)