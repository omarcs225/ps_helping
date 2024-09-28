# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        my_set = set()
        curr = headA
        
        while curr:
            if curr not in my_set:
                my_set.add(curr)
            curr = curr.next
        
        curr = headB
        
        while curr:
            if curr in my_set:
                return curr
            curr = curr.next
        return None