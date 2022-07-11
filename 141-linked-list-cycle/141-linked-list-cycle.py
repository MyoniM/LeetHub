# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = s = head
        x = 0
        while f and f.next:
            x += 1
            s = s.next
            f = f.next.next
            if s is f: return True
        return False