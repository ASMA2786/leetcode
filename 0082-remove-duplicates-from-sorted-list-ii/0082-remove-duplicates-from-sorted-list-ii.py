# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        temp = head

        while temp:
            if temp.next and temp.val == temp.next.val:
                value = temp.val

                while temp and temp.val == value:
                    temp = temp.next

                prev.next = temp
            else:
                prev = temp
                temp = temp.next

        return dummy.next