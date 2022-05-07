# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 =""
        num2 = ""
        itr1 = l1
        while itr1:
            num1+=str(itr1.val)
            itr1=itr1.next
        num1 = int(num1[::-1])

        itr2 = l2
        while itr2:
            num2+=str(itr2.val)
            itr2=itr2.next
        num2 = int(num2[::-1])
        
        res = num1 + num2
        dumb_node = ListNode(0)
        result = dumb_node
        for i in str(res)[::-1]:
            result.next = ListNode(int(i))
            result = result.next

        return dumb_node.next