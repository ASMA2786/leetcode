class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # suffix minimum
        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix[i] = min(nums[i], suffix[i + 1])

        # prefix maximum
        mx = nums[0]

        for i in range(n):
            mx = max(mx, nums[i])

            if mx - suffix[i] <= k:
                return i

        return -1