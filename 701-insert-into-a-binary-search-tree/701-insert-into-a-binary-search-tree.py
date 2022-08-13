# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return TreeNode(val)
        self.dfs(root, val)
        return root
    
    def dfs(self, node, val):
        if node.val < val:
            if node.right is None: node.right = TreeNode(val)
            else: self.dfs(node.right, val)
                
        if node.val > val:
            if node.left is None: node.left = TreeNode(val)
            else: self.dfs(node.left, val)