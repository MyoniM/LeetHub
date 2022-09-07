class Solution:
    def minDistance(self, str1: str, str2: str) -> int:
        n, m = len(str1), len(str2)
        cache = {}
        def dfs(i, j):
            if (i, j) in cache: return cache[(i, j)]
            if i>n or j>m: return float("inf")
            if i==n and j==m: return 0

            if not(i>=n or j>=m) and (str1[i] == str2[j]):
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]
            insert = dfs(i, j+1)
            delete = dfs(i+1, j)
            subs = dfs(i+1, j+1)
            cache[(i, j)] = 1+min(insert, delete, subs)
            return cache[(i, j)]
        return dfs(0, 0)