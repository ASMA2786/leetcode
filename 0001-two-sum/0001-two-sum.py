class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash={}
        for i in range(len(nums)):
            req=target-nums[i]
            if req in hash:
                return [i,hash[req]]
            else:
                hash[nums[i]]=i