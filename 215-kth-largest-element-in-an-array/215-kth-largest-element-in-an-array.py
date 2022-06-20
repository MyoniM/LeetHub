class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, -1 * n)
            
        while True:
            n = heapq.heappop(h)
            k -= 1
            if k == 0:
                return n * -1