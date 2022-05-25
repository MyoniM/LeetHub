# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        temp_next_pair = head.next.next
        temp_head = head
        head = head.next
        head.next = temp_head
        head.next.next = self.swapPairs(temp_next_pair)
        return head