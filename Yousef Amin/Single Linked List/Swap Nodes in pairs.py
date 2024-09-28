# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        i = 1
        prev,curr = None,head
        
        while curr:
            if i%2 ==0:
                prev.val , curr.val = curr.val , prev.val
            prev , curr = curr , curr.next
            i+=1
        return head