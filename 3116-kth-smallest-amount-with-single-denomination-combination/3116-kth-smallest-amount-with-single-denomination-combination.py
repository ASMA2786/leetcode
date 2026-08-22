class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        
        def lcm(a, b):
            return a // gcd(a, b) * b
        
        def count(x):
            ans = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                curr_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        curr_lcm = lcm(curr_lcm, coins[i])

                        if curr_lcm > x:
                            break

                        bits += 1

                else:
                    if bits % 2:
                        ans += x // curr_lcm
                    else:
                        ans -= x // curr_lcm

            return ans

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left