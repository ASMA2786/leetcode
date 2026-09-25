class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        for i in range(len(s)):
            value=ord(s[i])-ord('a')+1
            reverse=27-value
            prod=(i+1)*reverse
            sum+=prod
        return sum