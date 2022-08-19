# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque([root])
        
        while q:
            qSize = len(q)
            runningSum = 0 
            for _ in range(qSize):
                node = q.popleft()
                runningSum += node.val
                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)
            res.append(runningSum / qSize)
        return res