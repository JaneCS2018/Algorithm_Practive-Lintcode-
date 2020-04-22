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
    @return: true if it is a complete binary tree, or false.
    """
    def isComplete(self, root):
        # write your code here
        if root is None:
            return True
            
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index +=1
            
        while queue[-1] is None:
            queue.pop()
            
        for q in queue:
            if q is None:
                return False
        return True
