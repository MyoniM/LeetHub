class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [[p,s] for p,s in zip(position,speed)]
        s = []
        
        for p in sorted(pairs)[::-1]:
            speed = (target - p[0]) / p[1]
            if not s or s[-1] < speed: s.append(speed)
                
        return len(s)