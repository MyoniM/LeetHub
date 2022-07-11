# O(n * m) time | O(n + m) space
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''
        
        ct = Counter(t)
        req = len(ct)
        found = 0
        cs = {}
        l = r = 0
        ml = [None, None]
        while r < len(s):
            cs[s[r]] = cs.get(s[r], 0) + 1
            
            if s[r] in ct and cs[s[r]] == ct[s[r]]: found += 1 
                
            while l <= r and found == req:
                if ml[0] is None or (r - l + 1 < ml[1] - ml[0]):
                    ml[0], ml[1] = l, r + 1
                cs[s[l]] -= 1
                if s[l] in ct and cs[s[l]] < ct[s[l]]: found -= 1
                l += 1
            r += 1

        return "" if ml[0] is None else s[ml[0]: ml[1]]
