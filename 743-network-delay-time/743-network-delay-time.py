class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.getGraph(times)
        visited = set()
        minTimeHeap = [(0, k)]

        t = float('-inf')
        while minTimeHeap:
            currentDistance, node = heapq.heappop(minTimeHeap)
            
            if node in visited: continue
            visited.add(node)
            t = max(t, currentDistance)
            
            for edge in graph[node]:
                destination, distanceToDestination = edge
                newDistanceToDestination = distanceToDestination + currentDistance
                if destination not in visited:
                    heapq.heappush(minTimeHeap, (newDistanceToDestination, destination))
        
        return t if len(visited) == n else -1
    
    def getGraph(self, edges):
        graph = defaultdict(list)
        for k, v, w in edges:
            graph[k].append((v, w))
        return graph
