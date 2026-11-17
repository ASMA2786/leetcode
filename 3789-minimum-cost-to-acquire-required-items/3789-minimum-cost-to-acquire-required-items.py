
class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):

        a = need1 * cost1 + need2 * cost2

        b = max(need1, need2) * costBoth

        m = min(need1, need2)

        c = (m * costBoth +
             (need1 - m) * cost1 +
             (need2 - m) * cost2)

        return min(a, b, c)
