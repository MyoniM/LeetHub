class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.buildGraph(edges)
        visitedNodes = set()
        
        return self.depthFirstSearch(graph, source, destination, visitedNodes)
    
    def depthFirstSearch(self, graph, source, destination, visitedNodes):
        if source == destination: return True
        if source in visitedNodes: return False
        visitedNodes.add(source)
        
        for neighbor in graph[source]:
            if (self.depthFirstSearch(graph, neighbor, destination, visitedNodes) == True):
                return True
        return False
    
    # build adjacency list
    def buildGraph(self, edges):
        graph = defaultdict(list)
        for k, v in edges:
            graph[v].append(k)
            graph[k].append(v)
        return graph