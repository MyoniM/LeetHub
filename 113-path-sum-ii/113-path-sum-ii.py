# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node,a):
            if not node: return
            a = a[:]
            a.append(node.val)
            if not node.left and not node.right:
                if sum(a) == targetSum: res.append(a)
                return
            dfs(node.left, a)
            dfs(node.right, a)
        dfs(root, [])
        return res