class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)

        nums = set(nums)

        for i in range(1, n + 1):
            if i not in nums:
                ans.append(i)

        return ans