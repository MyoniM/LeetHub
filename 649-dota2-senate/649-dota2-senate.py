class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = deque(), deque()
        L = len(senate)
        for i, s in enumerate(senate):
            if s == "R": r.append(i)
            else: d.append(i)
        
        while r and d:
            ri, di = r.popleft(), d.popleft()
            if ri < di: r.append(ri + L)
            else: d.append(di + L)
                
        return "Dire" if d else "Radiant"