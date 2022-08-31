class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 0, min(time) * totalTrips
        while l <= r:
            m = (l + r)// 2
            trips = 0
            for t in time: 
                trips += m // t 
            if trips >= totalTrips:
                r = m - 1
            else:
                l = m + 1
        return l