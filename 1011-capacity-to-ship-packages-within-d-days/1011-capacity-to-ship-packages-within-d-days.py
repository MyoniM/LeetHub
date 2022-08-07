class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            if self.shipDays(m, weights) <= days:
                r = m - 1
            else:
                l = m + 1
        return l
    
    def shipDays(self, capacity, weights):
        day = 1
        cap = 0
        for n in weights:
            cap += n
            if cap > capacity:
                day += 1
                cap = n
        return day