
class Solution(object):
    def numOfSubarrays(self, arr):
        mod = 10**9 + 7

        odd = 0
        even = 1
        total = 0
        res = 0

        for num in arr:
            total += num

            if total % 2 == 0:
                res += odd
                even += 1
            else:
                res += even
                odd += 1

        return res % mod
