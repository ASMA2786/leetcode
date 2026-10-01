# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        k=k%length
        if k == 0:
            return head
        temp=head
        for _ in range(length-k-1):
            temp=temp.next
        s=temp.next
        temp.next=None
        last=s
        while last.next:
            last=last.next
        last.next=head
        return s
        
        