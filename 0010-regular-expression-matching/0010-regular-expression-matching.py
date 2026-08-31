class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_p = len(p)
        stack = list(p)
        past = [None]
        length = len(s)
        answer = [False]
        def helper(i,stack):
            #print(f"{stack} and {s[:i+1]}")
            if answer[0] or not stack or (i==-1 and not stack[-1] == '*'):
                if i == -1 and not stack:
                    answer[0] = True
                return
            present = stack.pop()
            #print(present)
            if present == s[i]:
                helper(i-1,stack[:])
            elif present == '.':
                helper(i-1,stack[:])
            elif present == '*':
                q = stack.pop()
                for num in range(length+len_p):
                    stack.extend([q]*num)
                    helper(i,stack[:])
                    for _ in range(num): stack.pop()
        helper(length-1,stack)
        return answer[0]
             
            