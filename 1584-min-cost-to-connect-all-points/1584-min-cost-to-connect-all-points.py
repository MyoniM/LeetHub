class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        L = len(points)
        
        adj = defaultdict(list)
        for i in range(L):
            xi, yi = points[i]
            for j in range(i + 1, L):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
                
        res = 0
        vis = set()
        minHeap = [[0,0]]
        while len(vis) != L:
            coast, i = heapq.heappop(minHeap)
            if i in vis: continue
            vis.add(i)
            res += coast
            for nc, n in adj[i]:
                if n not in vis: heapq.heappush(minHeap, [nc, n])
                    
        return res