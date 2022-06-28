# O(log(n)) time and space
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = self.helper(x, abs(n))
        # solve for +ve and return 1 / res if n was negative
        return res if n >= 0 else 1 / res
    
    def helper(self, x, n):
        if x == 0: return 0
        if n == 0: return 1
        res = self.helper(x, n // 2)
        # multiply the left half with the right
        res *= res
        return x * res if n % 2 else res  