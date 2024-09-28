# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        smaller = ListNode(0)
        greater = ListNode(0)
        curr_smaller = smaller
        curr_greater = greater
        curr = head
        
        while curr:
            if curr.val < x:
                curr_smaller.next = curr
                curr_smaller = curr_smaller.next
            else:
                curr_greater.next = curr
                curr_greater = curr_greater.next
            curr = curr.next
        
        curr_greater.next = None
        curr_smaller.next = None
        
        curr_smaller.next = greater.next
        return smaller.next