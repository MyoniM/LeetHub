"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0
        maxNodeCount = 0
        for node in root.children:
            maxNodeCount = max(maxNodeCount, self.maxDepth(node))
        return maxNodeCount + 1