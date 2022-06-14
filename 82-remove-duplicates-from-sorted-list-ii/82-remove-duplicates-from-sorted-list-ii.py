# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head: return head
        dummyNode = prevNode = ListNode(0, head)
        current = head
        while current and current.next is not None:
            if current.val == current.next.val:
                val = current.val
                while current and current.val == val:
                    current = current.next
            else:
                prevNode.next = current
                prevNode = current
                current = current.next
        prevNode.next = current
        return dummyNode.next