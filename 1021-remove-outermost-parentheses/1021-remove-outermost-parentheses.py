class Solution(object):
    def removeOuterParentheses(self, s):
        stack = []
        res = []

        for ch in s:
            if ch == '(':
                if stack:
                    res.append(ch)
                stack.append(ch)

            else:
                stack.pop()
                if stack:
                    res.append(ch)

        return ''.join(res)