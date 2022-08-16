# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        runningSum = [0]
        self.dfs(root, 0, runningSum)
        return runningSum[0]
    
    def dfs(self, node, currSum, runningSum):
        if node is None: return
        currSum = (currSum * 10) + node.val
        if node.left is None and node.right is None:
            runningSum[0] += currSum
        self.dfs(node.left, currSum, runningSum)
        self.dfs(node.right, currSum, runningSum)