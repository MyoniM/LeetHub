class Solution:
    def validateStackSequences(self, pu: List[int], po: List[int]) -> bool:
#         loop through pushed 
#         if s[-1] is popped[0]
#            yes: pop from s and popped while not same
#            no: add to s
#         return s is empty
        s = []
        for e in pu:
            if s and s[-1] == po[0]:
                while s and s[-1] == po[0]:
                    s.pop()
                    po.pop(0)
                s.append(e)
            else: s.append(e)
        while s and s[-1] == po[0]:
            s.pop()
            po.pop(0)
        return not s