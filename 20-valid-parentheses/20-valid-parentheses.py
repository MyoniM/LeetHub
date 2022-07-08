class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0 : return False
        op = ["(","{","["]
        cd = [")","}","]"]
        stack = []
        for i in range(len(s)):
            if s[i] in op: stack.append(s[i])
            else:
                if not stack: return False
                cb = s[i]
                cbi = cd.index(cb)
                ob = op[cbi]
                if stack[-1] != ob: return False
                stack.pop()
        return (not stack)
