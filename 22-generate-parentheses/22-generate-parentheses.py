class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # we need to have n open and closed brackets
        self.helper(n, n, [], res)
        return res
        
    def helper(self, l, r, b, res):
        # if we used all open and closed brackets, append to result
        if l + r == 0:
            res.append("".join(b))
            return
        # we can continue if we have open brackets
        if l > 0: self.helper(l - 1, r, b + ["("], res)
        # we can also continue to close if there is an open bracket
        if l < r: self.helper(l, r - 1, b + [")"], res)

#   n = 3
#                   3, 3
#                     |   <- we cant close a bracket without opening so we wont decrease the right
#                   2, 3
#                  /    \
#               1, 3    2, 2    <- either open another left or close the opened bracket
# continue until their sum == 0 (no more open or close brackets) and add the comination to result
        