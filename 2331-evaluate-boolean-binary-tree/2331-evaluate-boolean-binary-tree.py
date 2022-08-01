# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, node: Optional[TreeNode]) -> bool:
        VAL_MAP = {
            0: False,
            1: True
        }
        if node.left is None: return VAL_MAP[node.val]
        return self.dfsHelper(node, VAL_MAP)
        
    def dfsHelper(self, node, VAL_MAP):
        if node.left is None and node.right is None:
            return VAL_MAP[node.val]
        
        return self.dfsHelper(node.left, VAL_MAP) and self.dfsHelper(node.right, VAL_MAP) if node.val == 3 else self.dfsHelper(node.left, VAL_MAP) or  self.dfsHelper(node.right, VAL_MAP)