# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum) -> List[List[int]]:
        res = []
        self.do(root, targetSum, 0, [], res)
        return res
    def do(self, root, targetSum, runningSum, path, res):
        if not root: return
        if root.left is None and root.right is None and runningSum + root.val == targetSum:
            res.append(path + [root.val])
            return    
        self.do(root.left, targetSum, runningSum + root.val, path[:] + [root.val], res)
        self.do(root.right, targetSum, runningSum + root.val, path[:] + [root.val], res)
        return res