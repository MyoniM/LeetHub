class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        l = r = mx = 0
        while r < len(s):
            c[s[r]] = c.get(s[r],0) + 1
            r += 1
            while (r - l) - self.gmf(c) > k:
                c[s[l]] -= 1
                l += 1
            mx = max(mx, r - l)
        return mx
    
    def gmf(self, c):
        mx = 0
        for v in c.values():
            mx = max(v, mx)
        return mx