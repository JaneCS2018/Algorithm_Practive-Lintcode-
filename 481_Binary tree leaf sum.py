"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leafSum(self, root):
        # write your code here
        p = []
        self.dfs(root, p)
        return sum(p)
    
    def dfs(self, root, p):
        if root is None:
            return 
        if root.left is None and root.right is None:
            p.append(root.val)
        self.dfs(root.left, p)
        self.dfs(root.right,p)
