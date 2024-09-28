# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        def helper(root,cur_sum):
            if not root:
                return False
            if not root.left and not root.right:
                return cur_sum == targetSum
            
            return helper(root.left, cur_sum) or helper(root.right, cur_sum)
        return helper(root, cur_sum=0)
            