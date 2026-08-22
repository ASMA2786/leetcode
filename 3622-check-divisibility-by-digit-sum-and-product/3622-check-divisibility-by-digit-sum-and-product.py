class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        prod=1
        for ch in str(n):
            sum+=int(ch)
            prod*=int(ch)
        total=sum+prod
        if n % total==0:
            return True
        else:
            return False