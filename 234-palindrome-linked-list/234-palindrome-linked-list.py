# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) time | O(1) space
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        firstHalfListHead = head
        reversedListHead = self.reverseLinkedList(slow)
        while reversedListHead is not None:
            if firstHalfListHead.val != reversedListHead.val:
                return False
            firstHalfListHead = firstHalfListHead.next
            reversedListHead = reversedListHead.next
        return True
    
    def reverseLinkedList(self, head):
        prevNode, currentNode = None, head
        while currentNode is not None:
            tempNext = currentNode.next 
            currentNode.next = prevNode 
            prevNode = currentNode 
            currentNode = tempNext
        return prevNode
        
