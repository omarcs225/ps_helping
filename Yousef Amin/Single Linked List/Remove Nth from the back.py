# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        Dummy = ListNode(0)
        Dummy.next = head
        l = 0
        curr = head
        
        while curr:
            l+=1
            curr = curr.next
        
        index = l-n
        curr = head
        prev = Dummy
        i = 0
        
        while curr:
            if i==index:
               prev.next = curr.next
               return Dummy.next
            i+=1
            prev , curr = curr , curr.next
