class Solution:
    def firstUniqChar(self, s: str) -> int:
        hs = Counter(s)
        for i,e in enumerate(s):
            if hs[e] == 1: return i
        return -1