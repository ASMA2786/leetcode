class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                duplicate=nums[i]
                break
        for i in range(1, len(nums) + 1):
            if i not in nums:
                missing = i
                break
        return [duplicate, missing]
            