# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeInfo:
    def __init__(self, ancestor, depth):
        self.ancestor = ancestor
        self.depth = depth

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        treeInfo = self.dfs(root)
        return treeInfo.ancestor
    
    def dfs(self, node):
        if node is None: return TreeInfo(None, 0)
                
        leftStatus = self.dfs(node.left)
        rightStatus = self.dfs(node.right)

        if leftStatus.depth > rightStatus.depth:
            leftStatus.depth +=1
            return leftStatus
        elif leftStatus.depth < rightStatus.depth:
            rightStatus.depth +=1
            return rightStatus
        else: return TreeInfo(node, leftStatus.depth + 1)