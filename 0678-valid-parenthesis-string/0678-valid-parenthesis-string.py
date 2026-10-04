class Solution(object):
    def checkValidString(self, s):
        stack = []
        star = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)

            elif s[i] == '*':
                star.append(i)

            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while stack:
            if not star:
                return False

            if stack[-1] > star[-1]:
                return False

            stack.pop()
            star.pop()

        return True