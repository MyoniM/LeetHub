# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        currentNode = head
        neighborNode = head  

        while currentNode is not None:
            if counter >= n + 1:
                neighborNode = neighborNode.next
            currentNode = currentNode.next
            counter += 1

        if counter == n:
            if head.next is not None:
                head.val = head.next.val
                head.next = head.next.next
            else:
                return None
        else:
            neighborNode.next = neighborNode.next.next
        
        return head