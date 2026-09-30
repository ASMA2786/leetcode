# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return None
        len=0
        temp=head
        while temp:
            len+=1
            temp=temp.next
        mid=len//2
        temp=head
        prev=None
        for _ in range(mid):
            prev=temp
            temp=temp.next
        root=TreeNode(temp.val)
        if prev:
            prev.next=None
            root.left=self.sortedListToBST(head)
        
        root.right=self.sortedListToBST(temp.next)
        return root