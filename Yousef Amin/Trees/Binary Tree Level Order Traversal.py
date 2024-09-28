# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root) :
        
        lst = deque()
        lst.append(root)
        curr_lst = []
        res = []
        
        while lst:
            
            for i in range(len(lst)):
                
                node = lst.popleft()
                curr_lst.append(node.val)
                
                if node.left:
                    lst.append(node.left)
                
                if node.right:
                    lst.append(node.right)
            
            res.append(curr_lst)
            curr_lst = []
        
        return res