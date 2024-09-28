# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        curr = head
        while curr:
            start = curr.next
            while start:
                if start.val <=curr.val:
                    start.val , curr.val = curr.val , start.val
                start = start.next
            curr = curr.next
        return head