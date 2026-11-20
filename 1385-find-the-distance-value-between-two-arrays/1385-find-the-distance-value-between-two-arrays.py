class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        ans = 0

        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    break
            else:
                ans += 1

        return ans