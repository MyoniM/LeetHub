class Solution:
    def numEnclaves(self, matrix: List[List[int]]) -> int:
        onesConnectedToBorder = set()
        self.dfsBorders(matrix, onesConnectedToBorder)

        rowLength = len(matrix)
        colLength = len(matrix[0])
        count = 0
        for r in range(1, rowLength - 1):
            for c in range(1, colLength - 1):
                node = self.getStrNode(r, c)
                if matrix[r][c] == 1 and node not in onesConnectedToBorder:
                    count += 1
        return count 
    
    def dfsBorders(self, matrix, onesConnectedToBorder):
        rowLength = len(matrix)
        colLength = len(matrix[0])

        # top
        for i in range(colLength):
            self.dfSearch(matrix, 0, i, onesConnectedToBorder)
        # bottom    
        for i in range(colLength):
            self.dfSearch(matrix, rowLength - 1, i, onesConnectedToBorder)
        # left
        for i in range(rowLength):
            self.dfSearch(matrix, i, 0, onesConnectedToBorder)
        # right
        for i in range(rowLength):
            self.dfSearch(matrix, i, colLength - 1, onesConnectedToBorder)

    def dfSearch(self, matrix, r, c, onesConnectedToBorder):
        rowInbound = 0 <= r and r < len(matrix)
        colInbound = 0 <= c and c < len(matrix[0])
        if not rowInbound or not colInbound: return 

        if matrix[r][c] == 0: return 

        node = self.getStrNode(r, c)
        if node in onesConnectedToBorder: return 
        onesConnectedToBorder.add(node)

        # dfs neighbors
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            self.dfSearch(matrix, r + dr, c + dc, onesConnectedToBorder)

    def getStrNode(self, r, c):
        return "{} {}".format(r, c)