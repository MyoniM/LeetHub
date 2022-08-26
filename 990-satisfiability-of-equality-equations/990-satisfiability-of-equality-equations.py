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
    def equationsPossible(self, equations: List[str]) -> bool:
        ds = DS()
        for ex in equations:
            if ex[1] == "=":
                ds.union(ex[0], ex[3])
        
        for ex in equations:
            if ex[1] == "!":
                if ds.find(ex[0]) == ds.find(ex[3]): return False
        return True