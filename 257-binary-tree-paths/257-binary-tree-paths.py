# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None: return []
        if not root.left and not root.right:
            return [str(root.val)]
        path = [str(root.val) + "->" + p for p in  self.binaryTreePaths(root.left)]
        path += [str(root.val) + "->" + p for p in  self.binaryTreePaths(root.right)]
        return path