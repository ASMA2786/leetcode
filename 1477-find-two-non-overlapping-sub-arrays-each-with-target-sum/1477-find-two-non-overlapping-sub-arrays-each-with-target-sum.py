class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        dp = [float('inf')] * n

        left = 0
        curr_sum = 0
        ans = float('inf')
        best = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                if left > 0 and dp[left - 1] != float('inf'):
                    ans = min(ans, dp[left - 1] + length)

                best = min(best, length)

            dp[right] = best

        return -1 if ans == float('inf') else ans