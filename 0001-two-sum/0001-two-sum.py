class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash={}
        for i in range(len(nums)):
            if target-nums[i] in hash:
                return [hash[target-nums[i]],i]
            else:
                hash[nums[i]]=i

