class Solution:
    def nodesBetweenCriticalPoints(self, head):
        first = -1
        last = -1

        min_dist = float('inf')
        index = 1

        prev = head
        curr = head.next

        while curr.next:

            # Check if curr is a critical point
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                # First critical point
                if first == -1:
                    first = index

                # Another critical point
                else:
                    min_dist = min(min_dist, index - last)

                # Update latest critical point
                last = index

            prev = curr
            curr = curr.next
            index += 1

        # Fewer than 2 critical points
        if first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]