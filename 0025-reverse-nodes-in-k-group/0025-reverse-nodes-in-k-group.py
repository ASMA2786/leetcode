
class Solution(object):
    def reverseKGroup(self, head, k):

        temp = head
        count = 0

        while temp and count < k:
            temp = temp.next
            count += 1

        if count < k:
            return head

        prev = None
        curr = head

        for i in range(k):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        head.next = self.reverseKGroup(curr, k)

        return prev
