# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        s = [0]
        self.dfs(root, s)
        return s[0]
    def dfs(self, root, s):
        if not root: return 0
        left = self.dfs(root.left, s)
        right = self.dfs(root.right, s)
        s[0] += abs(left - right)
        return root.val + left + right
