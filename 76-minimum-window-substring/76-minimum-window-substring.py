class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count chars of T
        # search for a window in S that has all counts of T
        
        if len(t) > len(s): return ''
        
        ct = Counter(t)
        cs = {}
        
        l = r = 0
        ml = [None, None]
        
        while r < len(s):
            cs[s[r]] = cs.get(s[r], 0) + 1
            r += 1
            
            while self.sHasT(cs, ct):
                if ml[0] is None or (r - l < ml[1] - ml[0]):
                    ml[0], ml[1] = l, r
                cs[s[l]] -= 1
                l += 1
        
        return "" if ml[0] is None else s[ml[0]: ml[1]]
        
        
    def sHasT(self, cs,ct):
        for k in ct:
            if k not in cs or cs[k] < ct[k]:
                return False
        return True