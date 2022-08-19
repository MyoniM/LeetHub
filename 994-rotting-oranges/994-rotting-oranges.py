class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOrangesCount, rottenOranges = self.getOrangesCount(grid)
        if freshOrangesCount == 0: return 0
        rottenOragesQ = deque(rottenOranges)
        minute = 0
        freshOrangesToRot = 0
        rottenOrangesCount = len(rottenOranges)
        while rottenOragesQ:
            minute += 1
            rottenOragesSize = len(rottenOragesQ)
            freshOrangesToRot += rottenOragesSize
            for _ in range(rottenOragesSize):
                rottenOrange = rottenOragesQ.popleft()
                neighbors = self.getNeighbors(rottenOrange, grid)
                for neighbor in neighbors: rottenOragesQ.append(neighbor)
        return minute - 1 if (freshOrangesToRot - rottenOrangesCount) == freshOrangesCount else -1
    
    def getNeighbors(self, rottenOrange, grid):
        neighbors = []
        row, col = rottenOrange
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            newCell = (row + dr, col + dc)
            if self.isValidCell(newCell, grid):
                neighbors.append(newCell)
                grid[row + dr][col + dc] = 2
        return neighbors
    
    def isValidCell(self, newCell, grid):
        lenR, lenC = len(grid), len(grid[0])
        row, col = newCell
        if row in range(lenR) and col in range(lenC) and grid[row][col] == 1:
            return True
        return False
    
    def getOrangesCount(self, grid):
        freshOrangesCount = 0
        rottenOranges = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1: freshOrangesCount += 1
                elif grid[row][col] == 2: rottenOranges.append((row, col))
        return (freshOrangesCount, rottenOranges)
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               