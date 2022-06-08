# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1

        p1 = list1
        p1Prev = None
        p2 = list2
        
        while p1 is not None and p2 is not None:

            if p1.val < p2.val:
                p1Prev = p1
                p1 = p1.next
            else:
                if p1Prev is not None:
                    p1Prev.next = p2
                p1Prev = p2 # 1
                p2 = p2.next
                p1Prev.next = p1
        
        if p1 is None:
            p1Prev.next = p2 
        
        return list1 if list1.val < list2.val else list2