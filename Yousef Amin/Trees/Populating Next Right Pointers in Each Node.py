# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:06:23 2024

@author: Home
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def connect(self, root) :
        
        lst = deque()
        lst.append(root)
        curr_lst = []
        res = []
        
        if not root:
            return None
        
        while lst:
            
            for i in range(len(lst)):
                
                node = lst.popleft()
                curr_lst.append(node)
                
                if node.left:
                    lst.append(node.left)
                
                if node.right:
                    lst.append(node.right)
            
            for index,node in enumerate(curr_lst):
                
                if index != len(curr_lst)-1:
                    node.next = curr_lst[index+1]
                    
            curr_lst = []
        
        return root