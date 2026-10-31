class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=prices[0]
        profit=0
        for i in range(len(prices)):
            min_price=min(min_price,prices[i])
            profit =max(profit,prices[i]-min_price)
        return profit