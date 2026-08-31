class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def dfs(i, j):

            # Pattern finished
            if j == len(p):
                return i == len(s)

            # Have we already solved this?
            if (i, j) in memo:
                return memo[(i, j)]

            # Does current character match?
            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            # If next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':

                # Option 1: use 0 occurrences
                skip = dfs(i, j + 2)

                # Option 2: use 1 or more occurrences
                use = first_match and dfs(i + 1, j)

                ans = skip or use

            else:
                # Normal character or '.'
                ans = first_match and dfs(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)