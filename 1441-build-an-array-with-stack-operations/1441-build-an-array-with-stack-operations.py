class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        j = 0

        for i in range(1, n + 1):
            if j == len(target):
                break

            ans.append("Push")

            if target[j] == i:
                j += 1
            else:
                ans.append("Pop")

        return ans