# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

# O(nlog(k)) time | o(n) space
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyNode = newHead = ListNode(0)
        
        q = PriorityQueue()
        
        for head in lists:
            if head:
                q.put(PriorityNode(head))
            
        while not q.empty():
            next_node = q.get().node
            dummyNode.next = next_node
            dummyNode = dummyNode.next
            
            if next_node.next is not None:
                q.put(PriorityNode(next_node.next))
                
        return newHead.next

# Make objects comparable
# Read more at: https://stackoverflow.com/questions/40205223/priority-queue-with-tuples-and-dicts
class PriorityNode(object):
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val