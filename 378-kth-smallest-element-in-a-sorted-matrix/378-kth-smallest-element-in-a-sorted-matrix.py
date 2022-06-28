class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        length = len(matrix) - 1
        l, r = matrix[0][0], matrix[length][length]
        
        while l < r:
            mid = (l + r) // 2
            count = self.counter(matrix, mid)
            if count >= k: r = mid
            else: l = mid + 1
        return l
    
    def counter(self, matrix, mid):
        count = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] > mid:
                    break
                count += 1
        return count
    
    