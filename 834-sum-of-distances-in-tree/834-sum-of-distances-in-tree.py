# class Solution:
#     def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
#         graph = self.getGraph(edges)
#         print(graph)
#         answer = [0] * n
#         for node in range(n):
#             result = self.dfsGraph(node, graph, 0, set())
#             answer[node] = result
#             break
#         return answer
    
#     def dfsGraph(self, node, graph, s, vis):
#         if node in vis: return 0
#         vis.add(node)
#         rs = 0
#         for neighbour in graph[node]:
#             if neighbour in vis: continue
#             result = self.dfsGraph(neighbour, graph, s + 1, vis)
#             rs += result
#         if node == 2: print(rs + s)
#         return rs + s
            
#     def getGraph(self, edges):
#         graph = defaultdict(list)
#         for edge in edges:
#             ai = edge[0]
#             bi = edge[1]
#             graph[ai].append(bi)
#             graph[bi].append(ai)
            
#         return graph

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N
        def dfs(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans