class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        op=['+','-','*','/']
        for ch in tokens:
            if ch not in op:
                stack.append(int(ch))
            else:
                a=stack.pop()
                b=stack.pop()
                if ch=='+':
                    stack.append(a+b)
                if ch=='-':
                    stack.append(b-a)
                if ch=='*':
                    stack.append(a*b)
                if ch=='/':
                    stack.append(int(float(b)/float(a)))
        return stack[-1]
                


