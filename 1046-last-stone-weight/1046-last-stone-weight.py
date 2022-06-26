class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
    
        while len(maxHeap) > 0:
            if len(maxHeap) == 1: return -heapq.heappop(maxHeap)
            stnOne = -heapq.heappop(maxHeap)
            stnTwo = -heapq.heappop(maxHeap)
            if stnOne > stnTwo: heapq.heappush(maxHeap, -(stnOne - stnTwo))
        return 0