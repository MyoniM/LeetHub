class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        if n < 2: return n    
        
        if n in cache:
            result = cache[n]
        else:
            result = self.fib(n - 1) + self.fib(n - 2)
        
        cache[n] = result
        
        return result