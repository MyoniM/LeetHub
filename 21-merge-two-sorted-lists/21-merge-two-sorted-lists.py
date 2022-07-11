# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1

        c1 = list1
        c2 = list2
        d = c = ListNode(0)
        
        while c1 or c2:
            if c1 is None: 
                c.next = c2
                break
            if c2 is None: 
                c.next = c1
                break
                
            if c1.val <= c2.val:
                c.next = c1
                c1 = c1.next
            else:                
                c.next = c2
                c2 = c2.next
            c = c.next
        return d.next