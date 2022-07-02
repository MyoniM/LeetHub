class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHeap = []
        reachedBuilding = 0
        length = len(heights)
        
        for reachedBuildingIdx in range(length):
            if reachedBuildingIdx == length - 1: return reachedBuildingIdx
            
            heightDiff = heights[reachedBuildingIdx + 1] - heights[reachedBuildingIdx]
            
            if heightDiff <= 0: continue
                
            if bricks >= heightDiff:
                heapq.heappush(maxHeap, heightDiff * -1)
                bricks -= heightDiff
                
            elif ladders > 0:
                if len(maxHeap):
                    biggestBrickMove = maxHeap[0] * -1
                    if biggestBrickMove >= heightDiff:
                        bricks += biggestBrickMove
                        heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap, heightDiff * -1)
                        bricks -= heightDiff
                ladders -= 1
            else: break

        return reachedBuildingIdx

                        
                        