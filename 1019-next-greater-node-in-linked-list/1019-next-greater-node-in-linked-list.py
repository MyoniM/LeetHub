# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        answer = [] 
        
        currentNode = head
        idx = 0
        while currentNode is not None:
            answer.append(0)
            while stack and stack[-1][0] < currentNode.val:
                _, i = stack.pop()
                answer[i] = currentNode.val
            
            stack.append([currentNode.val, idx])
            currentNode = currentNode.next
            idx += 1
        
        return answer
