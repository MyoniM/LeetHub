class DS:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.rank[node] = 0
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])
    
    def union(self, node1, node2):
        find1, find2 = self.find(node1), self.find(node2)
        if find1 == find2: return False
        if self.rank[find1] > self.rank[find2]:
            self.parent[find2] = find1
            self.rank[find1] += 1
        else:
            self.parent[find1] = find2
            self.rank[find2] += 1
        return True
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ds = DS()
        L = len(isConnected)
        for r in range(L):
            for c in range(L):
                if r == c: continue
                if isConnected[r][c] != 1: continue
                ds.union(r, c)
        
        parents = set()
        for i in  range(L):
            parents.add(ds.find(i))
            
        return len(parents)