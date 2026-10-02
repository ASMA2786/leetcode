class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr=''
        max_length=0
        for i in range(len(s)):
            if s[i] not in curr:
                curr+=s[i]
                max_length=max(len(curr),max_length)
            else:
                while s[i] in curr:
                    curr=curr[1:]
                curr+=s[i]
                max_length=max(len(curr),max_length)
        return max_length

            

