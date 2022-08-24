class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for crs, prereq in prerequisites:
            graph[crs].append(prereq)
            
        visited = set()
        visiting = set()

        courseOrder = []
        def dfs(crs, visited, visiting, courseOrder):
            if crs in visiting: return False
            if crs in visited: return True
            
            visiting.add(crs)

            for prereq in graph[crs]:
                if not dfs(prereq, visited, visiting, courseOrder): return False
            
            graph[crs] = []
            visited.add(crs)
            visiting.remove(crs)
            courseOrder.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs, visited, visiting, courseOrder): return []
        return courseOrder