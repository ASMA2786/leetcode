class Solution:
    
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""

        for left in range(len(s)):
            ones = 0

            for right in range(left, len(s)):
                ones += (s[right] == '1')

                if ones == k:
                    cur = s[left:right + 1]

                    if ans == "" or len(cur) < len(ans) or (
                        len(cur) == len(ans) and cur < ans
                    ):
                        ans = cur

                    break

        return ans