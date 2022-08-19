class Solution:
    def isSameTree(self, node1, node2):
        if node1 is None and node2 is None: return True
        if node1 is None or node2 is None: return False
        if node1.val != node2.val: return False
        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)