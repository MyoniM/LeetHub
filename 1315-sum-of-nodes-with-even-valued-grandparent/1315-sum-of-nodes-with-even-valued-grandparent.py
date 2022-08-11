# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = [0]
        def dfs(root):
            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        res[0] += root.left.left.val
                    if root.left.right:
                        res[0] += root.left.right.val
                if root.right:
                    if root.right.left:
                        res[0] += root.right.left.val
                    if root.right.right:
                        res[0] += root.right.right.val
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        return res[0]