class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            l, r = 0, len(row)
            while l<r:
                mid = (l + r) // 2
                if row[mid]<0:
                    r = mid
                else:
                    l = mid+1
            count += len(row) - l
        return count