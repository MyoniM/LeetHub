class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l = len(isConnected)
        visited = set()
        
        count = 0
        for i in range(l):
            if i not in visited:
                self.dfs(i, isConnected, visited)
                count += 1
        return count
    
    def dfs(self, i, isConnected, visited):
        for j, val in enumerate(isConnected[i]):
            if val == 1 and j not in visited:
                visited.add(j)
                self.dfs(j, isConnected, visited)
