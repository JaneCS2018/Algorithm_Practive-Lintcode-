"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a mirror of itself, or false.
    """
    def help(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.help(p.left, q.right) and self.help(p.right, q.left)
        return False
           
    def isSymmetric(self, root):
        if root:
            return self.help(root.left, root.right)
        return True
