# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        lst = self.Reverse(slow.next)
        slow.next = None
        
        dummy = ListNode(0)
        curr = dummy
        curr1 = head
        curr2 = lst
        
        while curr2 or curr1:
            if curr1:
                curr.next = curr1
                curr = curr.next
                curr1 = curr1.next
            if curr2:
                curr.next = curr2
                curr = curr.next
                curr2 = curr2.next
            
        return dummy.next
    
    def Reverse(self,head):
        prev,curr = None,head
        while curr:
            temp = curr.next
            curr.next = prev
            prev,curr = curr,temp
        return prev