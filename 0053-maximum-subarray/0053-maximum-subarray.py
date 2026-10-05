class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr=nums[0]
        maxi=nums[0]
        for i in range(1,len(nums)):
            curr=max(curr+nums[i],nums[i])
            maxi=max(maxi,curr)
        return maxi