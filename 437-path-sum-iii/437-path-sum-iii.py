# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None: return 0
        pathCount = [0]
        self.dfsHelper(root, 0, pathCount, {0:1}, targetSum)
        return pathCount[0]
    
    def dfsHelper(self, node, currentSum, pathCount, memo, targetSum):
        currentSum += node.val
        diff = currentSum - targetSum
        pathCount[0] += memo.get(diff, 0)
        memo[currentSum] = 1 + memo.get(currentSum, 0)
        if node.left: self.dfsHelper(node.left, currentSum, pathCount, dict(memo), targetSum)
        if node.right: self.dfsHelper(node.right, currentSum, pathCount, dict(memo), targetSum)