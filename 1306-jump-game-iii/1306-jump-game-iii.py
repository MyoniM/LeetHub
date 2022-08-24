class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        lenArr = len(arr)
        q = deque([start])
        vis = set()
        while q:
            for _ in range(len(q)):
                idx = q.popleft()
                vis.add(idx)
                if arr[idx] == 0: return True
                if self.isValidIdx(idx + arr[idx], lenArr, vis): q.append(idx + arr[idx])
                if self.isValidIdx(idx - arr[idx], lenArr, vis): q.append(idx - arr[idx])
        return False
    
    def isValidIdx(self, idx, lenArr, vis):
        return idx >= 0 and idx < lenArr and idx not in vis
            