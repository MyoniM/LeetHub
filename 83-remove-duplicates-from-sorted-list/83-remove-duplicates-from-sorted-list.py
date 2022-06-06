# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            tempVal = current.val
            while current.next and current.next.val == tempVal:
                current.next = current.next.next
            current = current.next
        return head