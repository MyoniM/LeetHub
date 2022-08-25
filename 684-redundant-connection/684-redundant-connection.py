class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        
    def union(self, x, y):
        findX, findY = self.find(x), self.find(y)
        if findX != findY:
            if self.rank[findX] > self.rank[findY]:
                self.parent[findY] = findX
                self.rank[findX] += 1
            else:
                self.parent[findX] = findY
                self.rank[findY] += 1
            
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()
        for a, b in edges:
            if uf.find(a) == uf.find(b):
                return [a, b]
            uf.union(a, b)
        