"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        q = deque([root])
        r = []
        while q:
            l = []
            for _ in range(len(q)):
                n = q.popleft()
                l.append(n.val)
                for node in n.children:
                    q.append(node)
            r.append(l)
        return r