class Solution:
    def reverseParentheses(self, s: str) -> str:
#       (ed(et(oc
#               (ed(etco
#                   (edocteel
#       stack = []
#       for loop through elems
#           if elem is not )
#               add to stack
#           else
#               while loop backwar till (
#                   append string
#               remove ( and put the string in the stack and continue
#       return the first element
        stack = []
        for e in s:
            if e != ")": stack.append(e)
            else:
                newS = ""
                while stack and stack[-1] != "(":
                    el = stack.pop()
                    newS = el + newS
                stack.pop()
                stack.append(newS[::-1])
        return ''.join(stack)