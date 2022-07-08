class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        
        s = []
        a = [0] * len(t)
        
        for i, e in enumerate(t):
            while s and e > t[s[-1]]:
                d = s.pop()
                a[d] = i - d                       
            s.append(i)
        return a