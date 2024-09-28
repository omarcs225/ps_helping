# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root) :
        
        lst = deque()
        lst.append(root)
        curr_lst = []
        res = []
        if not root:
            return []
        while lst:
            
            for i in range(len(lst)):
                
                node = lst.popleft()
                curr_lst.append(node.val)
                
                if node.left:
                    lst.append(node.left)
                
                if node.right:
                    lst.append(node.right)
            
            res.append(curr_lst[-1])
            curr_lst = []
        
        return res