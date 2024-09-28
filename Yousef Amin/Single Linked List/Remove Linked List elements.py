# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeElements(self, head, k):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        Dummy = ListNode(0)
        Dummy.next = head
        prev,curr = Dummy,head
        
        while curr:
            if curr.val == k :
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return Dummy.next