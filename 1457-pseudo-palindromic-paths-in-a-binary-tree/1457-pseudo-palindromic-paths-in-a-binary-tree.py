# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    palindromicPathCount = 0
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.dfsHelper(root, {})
        return self.palindromicPathCount
    
    def dfsHelper(self, root, counter):
        if not root: return
        counter[root.val] = 1 + counter.get(root.val, 0)
        self.dfsHelper(root.left, counter)
        self.dfsHelper(root.right, counter)
        if root.left is None and root.right is None:
            if self.isPalindrome(counter):
                self.palindromicPathCount += 1
        counter[root.val] -= 1

    def isPalindrome(self, counter):
        oddsCount = 0
        for value in counter.values():
            if oddsCount > 1: return False
            if value % 2 != 0: oddsCount += 1
        return oddsCount < 2