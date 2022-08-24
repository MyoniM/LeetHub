class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for crs, prereq in prerequisites:
            graph[crs].append(prereq)
            
        visited = set()
        def dfs(crs, visited):
            if crs in visited: return False
            if graph[crs] == []: return True
            
            visited.add(crs)
            for prereq in graph[crs]:
                if not dfs(prereq, visited): return False
            
            visited.remove(crs)
            graph[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs, visited): return False
        return True