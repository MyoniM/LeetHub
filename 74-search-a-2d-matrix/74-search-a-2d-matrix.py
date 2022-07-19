class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        colLen = len(matrix[0])
        rowLen = len(matrix)
        l, r = 0, (rowLen * colLen) - 1
        while l <= r:
            mid = (l + r) // 2
            row, col = self.getIdx(mid, colLen)
            currElem = matrix[row][col]
            if target == currElem: return True
            elif currElem > target: r = mid - 1
            else: l = mid + 1
        return False
    
    def getIdx(self, mid, colLen):
        row = mid // colLen
        col = mid % colLen
        return (row, col)
        