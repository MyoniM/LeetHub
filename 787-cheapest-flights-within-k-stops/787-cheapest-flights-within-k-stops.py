class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minPrice = [float("inf")] * n
        minPrice[src] = 0
        
        for _ in range(k + 1):
            tempPrice = minPrice.copy()
            for s, d, p in flights:
                if minPrice[s] == float("inf"): continue
                if minPrice[s] + p < tempPrice[d]:
                    tempPrice[d] = minPrice[s] + p
            minPrice = tempPrice
        return minPrice[dst] if minPrice[dst] != float("inf") else -1