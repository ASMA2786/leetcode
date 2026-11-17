
class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        res = float('inf')

        for i in range(len(nums)):
            total = 0

            for j in range(i, len(nums)):
                total += nums[j]

                length = j - i + 1

                if l <= length <= r and total > 0:
                    res = min(res, total)

        if res == float('inf'):
            return -1

        return res
