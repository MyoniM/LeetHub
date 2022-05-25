class Solution:
    
    def swap(self, s, l, r):
        if l >= r: return
        s[l], s[r] = s[r], s[l]
        self.swap(s,l+1,r-1)
        
    def reverseString(self, s: List[str]) -> None:
        l , r = 0, len(s) - 1
        self.swap(s,l,r)