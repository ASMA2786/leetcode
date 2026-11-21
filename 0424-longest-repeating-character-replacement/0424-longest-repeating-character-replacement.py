class Solution(object):
    def characterReplacement(self, s, k):
        freq = {}
        left = 0
        maxi = 0
        ans = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            maxi = max(maxi, freq[s[right]])

            if right - left + 1 - maxi > k:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans