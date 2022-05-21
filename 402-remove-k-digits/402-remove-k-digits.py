class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
  
        if k == len(num): return "0"
        
        s = []
        for i in num:
            while s and k > 0 and s[-1] > i:
                s.pop()
                # if s[-1] != i:
                k-=1
            s.append(i)
            
        s = s[:len(s)-k]
        return str(int("".join(s)))