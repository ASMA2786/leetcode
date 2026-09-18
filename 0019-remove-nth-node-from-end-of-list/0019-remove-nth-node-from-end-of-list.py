# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        length=0
        temp=head
        if not temp:
            return head
        while temp:
            length+=1
            temp=temp.next
        if n==length:
            return head.next
        temp=head
        for i in range(0,length-n-1):
            temp=temp.next
        temp.next=temp.next.next
        return head