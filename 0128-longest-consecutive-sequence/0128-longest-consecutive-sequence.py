class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        nums.sort()
        count=1
        max_c=1
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                count+=1
                max_c=max(max_c,count)
            elif nums[i]==nums[i+1]:
                continue
            else:
                count=1
        return max_c
    

