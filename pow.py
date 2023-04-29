x = 2.00000
n = 10


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        return res
        
instance = Solution()
print (instance.myPow(x , n))        