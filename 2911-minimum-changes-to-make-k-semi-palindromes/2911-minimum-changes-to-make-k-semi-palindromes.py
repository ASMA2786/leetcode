
class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)

        cost = [[float('inf')] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for r in range(d):
                        left = r
                        right = ((length - 1 - r) // d) * d + r

                        while left < right:
                            if s[i + left] != s[i + right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for p in range(1, k + 1):
                for j in range(0, i - 1):
                    if dp[j][p - 1] != float('inf'):
                        dp[i][p] = min(
                            dp[i][p],
                            dp[j][p - 1] + cost[j][i - 1]
                        )

        return dp[n][k]
