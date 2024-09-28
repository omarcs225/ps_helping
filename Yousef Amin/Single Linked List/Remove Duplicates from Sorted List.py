# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        prev , curr = None,head
        my_set = set()
        
        while curr:
            if curr.val not in my_set:
                my_set.add(curr.val)
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        return head