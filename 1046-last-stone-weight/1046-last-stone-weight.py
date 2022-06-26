class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [(-1 * s) for s in stones]
        heapq.heapify(maxHeap)
    
        while len(maxHeap) > 0:
            if len(maxHeap) == 1: return heapq.heappop(maxHeap) * -1
            stnOne = heapq.heappop(maxHeap) * -1
            stnTwo = heapq.heappop(maxHeap) * -1
            smashRes = 0 if stnOne == stnTwo else stnOne - stnTwo
            if smashRes != 0: heapq.heappush(maxHeap, smashRes * -1)
        return 0