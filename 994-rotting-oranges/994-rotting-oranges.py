class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # get rotten, count fresh
        visitedOranges = [[False] * len(grid[0]) for row in grid]

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
                neighbors = self.getNeighbors(rottenOrange, grid, visitedOranges)
                for neighbor in neighbors: rottenOragesQ.append(neighbor)
        return minute - 1 if (freshOrangesToRot - rottenOrangesCount) == freshOrangesCount else -1
    
    def getNeighbors(self, rottenOrange, grid, visitedOranges):
        neighbors = []
        row, col = rottenOrange
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            newCell = (row + dr, col + dc)
            if self.isValidCell(newCell, grid, visitedOranges):
                neighbors.append(newCell)
                visitedOranges[row + dr][col + dc] = True
        return neighbors
    
    def isValidCell(self, newCell, grid, visitedOranges):
        lenR, lenC = len(grid), len(grid[0])
        row, col = newCell
        if row in range(lenR) and col in range(lenC) and grid[row][col] == 1 and not visitedOranges[row][col]:
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
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               
                                                               