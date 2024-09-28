# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k==0:
            return head
        l = 0
        curr = head
        
        while curr:
            l+=1
            curr = curr.next
        k = k % l
        if not k:
            return head
        index = l - k
        i=0
        prev,curr = None,head
        for _ in range(index):
            prev,curr = curr,curr.next
        prev.next = None
        
        start = curr
        while curr.next:
            curr = curr.next
        curr.next = head
        return start