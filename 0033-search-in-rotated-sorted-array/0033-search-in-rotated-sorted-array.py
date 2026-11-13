class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not target in nums:
            return -1
        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i