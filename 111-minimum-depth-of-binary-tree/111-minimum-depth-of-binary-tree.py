# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeInfo:
    def __init__(self, minHeight):
        self.minHeight = minHeight
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        treeInfo = TreeInfo(float("inf"))
        self.dfs(root, 1, treeInfo)
        return treeInfo.minHeight
    
    def dfs(self, root, currentHeight, treeInfo):
        if root is None: return
        if root.left is None and root.right is None:
            treeInfo.minHeight = min(treeInfo.minHeight, currentHeight)
        self.dfs(root.left, currentHeight + 1, treeInfo)
        self.dfs(root.right, currentHeight + 1, treeInfo)