class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        
        left = top = 0
        right = bottom = n
        
        c = 1
        while left < right and top < bottom:
            for i in range(left, right):
                grid[top][i] = c
                c += 1
            top += 1
            
            for i in range(top, bottom):
                grid[i][right - 1] = c
                c += 1
            right -= 1
            
            if left >= right or top >= bottom: break


            for i in range(right - 1, left - 1, -1):
                grid[bottom - 1][i] = c
                c += 1
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1):
                grid[i][left] = c
                c += 1
            left += 1
            
            
            # break
        return grid