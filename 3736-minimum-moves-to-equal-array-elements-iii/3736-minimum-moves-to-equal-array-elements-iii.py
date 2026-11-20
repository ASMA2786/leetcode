class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        moves=0
        max_ele=max(nums)
        for i in range(len(nums)):
            while nums[i]!=max_ele:
                nums[i]+=1
                moves+=1
        return moves
