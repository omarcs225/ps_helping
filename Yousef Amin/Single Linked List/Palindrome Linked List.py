# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        lst = self.Reverse(slow)
        curr1 = lst
        curr2 = head
        
        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        return True
    
    def Reverse(self,head):
        
        prev,curr = None,head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev,curr = curr,temp
            
        return prev