class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        c1 = Counter(s1)
        if len(s2) < len(s1): return False
        
        c2 = {}
        l = r = 0
        while r < len(s2):
            c = s2[r] 
            c2[c] = c2.get(c, 0) + 1
            if r >= l1 - 1:
                # O(1) time
                flag = True
                for k in c1:
                    if k not in c2 or c2[k] != c1[k]:
                        flag = False
                        break
                if flag: return flag
                c2[s2[l]] -= 1
                l += 1
            r += 1
        return False