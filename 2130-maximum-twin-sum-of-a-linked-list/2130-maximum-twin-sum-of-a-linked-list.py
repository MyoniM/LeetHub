# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head.next
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            
        firstPtr = head
        midPtr = self.reverseLinkedList(slow)
        maxSum = float('-inf')
        
        while midPtr is not None:
            maxSum = max(firstPtr.val + midPtr.val, maxSum)
            midPtr = midPtr.next
            firstPtr = firstPtr.next
        
        return maxSum
    
    def reverseLinkedList(self, head):
        currentNode = head
        prevNode = None
        while True:
            tempNext = currentNode.next
            currentNode.next = prevNode
            if tempNext is None: break
            prevNode = currentNode
            currentNode = tempNext
        return currentNode