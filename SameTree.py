# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        res = [True]
        def helper(first,second):
            if not first and not second:
                return
            if (not first and second) or (first and not second):
                res[0] = False
                return
            if first.val != second.val:
                res[0] = False
            helper(first.left,second.left)
            helper(first.right, second.right)
        
        helper(p,q)
        return res[0]
            