class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for ele in freq:
            if freq[ele]> n//2:
                return ele