
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = []

        for i in range(len(nums1)):
            diff.append(abs(nums1[i] - nums2[i]))

        k = k1 + k2

        if sum(diff) <= k:
            return 0

        low = 0
        high = max(diff)

        while low < high:
            mid = (low + high) // 2

            ops = 0
            for d in diff:
                ops += max(0, d - mid)

            if ops <= k:
                high = mid
            else:
                low = mid + 1

        level = low
        used = 0
        ans = 0

        for d in diff:
            used += max(0, d - level)
            ans += min(d, level) ** 2

        rem = k - used
        ans -= rem * (2 * level - 1)

        return ans
