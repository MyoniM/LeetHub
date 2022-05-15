class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        
        s_count = Counter(s)
        t_count = Counter(t) 
        
        for e in s:
            if e not in t_count: return False
            if s_count[e] != t_count[e]: return False
            
        return True