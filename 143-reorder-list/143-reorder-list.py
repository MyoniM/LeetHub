# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next: return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        first = head
        tempNext = slow.next
        slow.next = None
        second = self.reverseLinkedList(tempNext)
        
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

    def reverseLinkedList(self, currentNode):
        prevNode = None
        while True:
            tempNext = currentNode.next
            currentNode.next = prevNode
            if tempNext is None: break
            prevNode = currentNode
            currentNode = tempNext
        return currentNode
        