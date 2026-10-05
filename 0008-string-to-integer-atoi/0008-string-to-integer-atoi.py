class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        sign=1
        i=0
        while i < len(s) and s[i] == ' ':
            i += 1 
        if i<len(s) and s[i] in ['-','+']:
            if s[i]=='-':
                sign=-1
            i=i+1
        num=0
        while i <len(s) and s[i].isdigit():
            num=num*10+int(s[i])
            i+=1
        num*=sign
        if num < -2**31:
            return -2**31

        if num > 2**31 - 1:
            return 2**31 - 1
        return num

