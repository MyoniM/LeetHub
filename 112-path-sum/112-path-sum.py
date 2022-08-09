class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.sumPath(root, 0, targetSum)
    
    def sumPath(self, root, runningSum, targetSum):
        if not root: return False
        
        if not root.left and not root.right and runningSum + root.val == targetSum:
            return True
        
        leftEqualsTarget = self.sumPath(root.left, runningSum + root.val, targetSum)
        rightEqualsTarget = self.sumPath(root.right, runningSum + root.val, targetSum)
        
        return leftEqualsTarget or rightEqualsTarget