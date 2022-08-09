class Solution:
    def __init__(self):
        self.DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startClr = image[sr][sc]
        self.fillColor(sr, sc, startClr, color, image, set())
        return image
    
    def fillColor(self, row, col, startClr, color, image, visited):
        if (row, col) in visited: return

        if row < 0 or row == len(image): return
        if col < 0 or col == len(image[0]): return
        
        visited.add((row, col))
        
        if image[row][col] != startClr: return
        image[row][col] = color
        
        for r, c in self.DIRECTIONS:
            self.fillColor(row + r, col + c, startClr, color, image, visited)
        