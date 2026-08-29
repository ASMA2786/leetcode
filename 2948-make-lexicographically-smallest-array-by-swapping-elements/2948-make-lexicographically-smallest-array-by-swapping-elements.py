class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # value, original index
        arr = sorted((nums[i], i) for i in range(n))

        ans = [0] * n

        i = 0

        while i < n:
            j = i

            # Find one connected group
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Values in this group
            values = [arr[k][0] for k in range(i, j + 1)]

            # Original indices in this group
            indices = sorted(arr[k][1] for k in range(i, j + 1))

            # Smallest values -> smallest indices
            for k in range(len(values)):
                ans[indices[k]] = values[k]

            i = j + 1

        return ans