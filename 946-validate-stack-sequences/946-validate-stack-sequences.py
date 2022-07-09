class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        s = []
        j = 0
        
        for i in pushed:
            s.append(i)
            
            while s and s[-1] == popped[j]:
                s.pop()
                j+=1
        return not s