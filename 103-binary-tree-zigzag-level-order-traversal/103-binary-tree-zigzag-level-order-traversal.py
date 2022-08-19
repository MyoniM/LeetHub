# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = deque([root])
        output = []
        traverseFromLeft = True
        while q:
            sameLvlNodes = []
            for _ in range(len(q)):
                node = q.popleft() if traverseFromLeft else q.pop()
                sameLvlNodes.append(node.val)
                if traverseFromLeft:
                    if node.left is not None: q.append(node.left)
                    if node.right is not None: q.append(node.right)

                else:
                    if node.right is not None: q.appendleft(node.right)
                    if node.left is not None: q.appendleft(node.left)
            output.append(sameLvlNodes)
            traverseFromLeft = not traverseFromLeft
            
        return output