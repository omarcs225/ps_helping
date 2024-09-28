class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(first, second):
            if not first and not second:
                return True  
            if not first or not second:
                return False  
            if first.val != second.val:
                return False  
            
            
            return helper(first.left, second.right) and helper(first.right, second.left)
        
        
        return helper(root, root) if root else True
