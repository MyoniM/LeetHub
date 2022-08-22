# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def push(s, root):
            while root:
                s.append(root)
                root = root.left
                
        def remove(s):
            n = s.pop()
            push(s, n.right)
            return n
        
        s = []
        push(s, root)
        sm = None
        for _ in range(k):
            sm = remove(s)
        return sm.val