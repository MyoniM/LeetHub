class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for e in s:
            if e == "]":
                word = ""
                num = ""
                while stack and stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * word)
            else: stack.append(e)
                
        return "".join(stack)   
            