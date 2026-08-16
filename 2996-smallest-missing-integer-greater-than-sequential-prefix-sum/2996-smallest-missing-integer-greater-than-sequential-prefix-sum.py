class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = nums[0]
        
        # Find sequential prefix sum
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break
        
        # Put all numbers in a set for O(1) lookup
        s = set(nums)

        # Find smallest missing integer >= total
        while total in s:
            total += 1

        return total