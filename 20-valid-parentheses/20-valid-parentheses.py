class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0 : return False
        op = ["(","{","["]
        cd = [")","}","]"]

        stack = []

        for b in s:
            if b in op: stack.append(b)
            else: 
                if len(stack) > 0 and stack.pop() == op[cd.index(b)]:
                    continue
                else: return False

        if len(stack) > 0: return False
        return True
