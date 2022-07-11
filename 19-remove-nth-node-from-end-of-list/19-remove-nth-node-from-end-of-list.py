# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tc = 0
        c = head
        while c:
            tc+=1
            c = c.next
        if tc == n == 1: return None
        if tc - n == 0: return head.next
            
        c = head
        x = 0
        while c:
            x += 1
            if x == tc - n:
                c.next = c.next.next
            c = c.next
            
        return head

        