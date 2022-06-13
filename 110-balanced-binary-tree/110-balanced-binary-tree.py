# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkIfBalanced(root).isBalanced
    
    def checkIfBalanced(self, node):
        if node is None: return HeightBalanceInfo(True, 0)

        leftNodeHeight = self.checkIfBalanced(node.left)
        rightNodeHeight = self.checkIfBalanced(node.right)

        if not leftNodeHeight.isBalanced or not rightNodeHeight.isBalanced:
            return HeightBalanceInfo(False, 0)

        if abs(leftNodeHeight.maxHeight - rightNodeHeight.maxHeight) < 2:
            maxHeight = max(leftNodeHeight.maxHeight, rightNodeHeight.maxHeight)
            return HeightBalanceInfo(True, 1 + maxHeight)
        return HeightBalanceInfo(False, 0)

class HeightBalanceInfo:
    def __init__(self, isBalanced, maxHeight):
        self.isBalanced = isBalanced
        self.maxHeight = maxHeight
        