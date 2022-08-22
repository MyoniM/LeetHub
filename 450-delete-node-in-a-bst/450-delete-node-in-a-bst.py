# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int, parentNode=None) -> Optional[TreeNode]:
        if not root: return
        hasUpdated = False
        inputRoot = root
        while root:
            if root.val > key:
                parentNode = root
                root = root.left
            elif root.val < key:
                parentNode = root
                root = root.right
            else:
                hasUpdated = True
                if root.left is not None and root.right is not None:
                    root.val = self.getMinValue(root.right)
                    self.deleteNode(root.right, root.val, root) 
                
                elif root.left is None and root.right is None:
                    if parentNode is None: return None
                    elif parentNode.left is root:
                        parentNode.left = root.left
                    else:
                        parentNode.right = root.right
                        
                elif root.left is not None:
                    if parentNode is None: return root.left
                    elif parentNode.left is root:
                        parentNode.left = root.left
                    else:
                        parentNode.right = root.left

                elif root.right is not None:
                    if parentNode is None: return root.right
                    elif parentNode.left is root:
                        parentNode.left = root.right
                    else:
                        parentNode.right = root.right
                break
        return inputRoot
    
    def getMinValue(self, root):
        while root.left: root = root.left
        return root.val