# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeInfo:
    def __init__(self, currentTotalSum, maxSum):
        self.currentTotalSum = currentTotalSum
        self.maxSum = maxSum
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.getTreeInfo(root).currentTotalSum
    
    def getTreeInfo(self, tree):
        if tree is None: return TreeInfo(float('-inf'), 0)

        leftTreeInfo = self.getTreeInfo(tree.left)
        rightTreeInfo = self.getTreeInfo(tree.right)

        value = tree.val
        maxSum = max(leftTreeInfo.maxSum, rightTreeInfo.maxSum)
        maxSumAsBranch = max(maxSum + value, value)

        currentSum = leftTreeInfo.maxSum + value + rightTreeInfo.maxSum
        maxSumWithRoot = max(currentSum, maxSumAsBranch)

        maxPathSum = max(leftTreeInfo.currentTotalSum, rightTreeInfo.currentTotalSum, maxSumWithRoot)

        return TreeInfo(maxPathSum, maxSumAsBranch)

