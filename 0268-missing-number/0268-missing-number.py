class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: in
        """
        nums.sort()
        for i in range(0,max(nums)):
            if i!=nums[i]:
                return i
        return max(nums)+1
            

