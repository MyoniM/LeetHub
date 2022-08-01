# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None: return 0
        ans = [0]
        self.dfsHelper(root, True, ans)
        return ans[0]
    
    def dfsHelper(self, node, isLeftNode, ans):
        if node is None: return 0
        if node.left is None and node.right is None and isLeftNode:
            ans[0] += node.val
        self.dfsHelper(node.left, True, ans)
        self.dfsHelper(node.right, False, ans) 
               