class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        idx1 = nums.index(max(nums))
        idx2 = nums.index(min(nums))

        a = min(idx1, idx2)
        b = max(idx1, idx2)

        option1 = b + 1
        option2 = n - a
        option3 = (a + 1) + (n - b)

        return min(option1, option2, option3)
        