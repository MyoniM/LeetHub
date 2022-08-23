# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def push(s, root):
            while root is not None:
                s.append(root)
                root = root.left
        def pop(s):
            node = s.pop()
            push(s, node.right)
            return node.val
        
        s1, s2, res = [], [], []
        push(s1, root1)
        push(s2, root2)

        while s1 or s2:
            if not s1: res.append(pop(s2))
            elif not s2: res.append(pop(s1))
            else:
                if s1[-1].val < s2[-1].val: res.append(pop(s1))
                else: res.append(pop(s2))
                    
        return res