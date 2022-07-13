class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, n, [], res)
        return res
        
    def helper(self, l, r, b, res):
        if l + r == 0:
            res.append("".join(b))
            return
        if l > 0: self.helper(l - 1, r, b + ["("], res)
        if l < r: self.helper(l, r - 1, b + [")"], res)

            
        