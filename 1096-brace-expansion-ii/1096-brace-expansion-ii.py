class Solution(object):
    def braceExpansionII(self, expression):
        def multiply(a, b):
            ans = set()

            for x in a:
                for y in b:
                    ans.add(x + y)

            return ans

        def dfs(s, i):
            result = set()
            current = {""}

            while i < len(s) and s[i] != '}':
                
                if s[i] == '{':
                    inside, i = dfs(s, i + 1)
                    current = multiply(current, inside)

                elif s[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1

                else:
                    current = multiply(current, {s[i]})
                    i += 1

            result.update(current)

            return result, i + 1

        ans, _ = dfs(expression, 0)

        return sorted(ans)