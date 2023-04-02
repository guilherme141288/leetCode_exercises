dividend = 10
divisor = 3

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        bit_num = 0
        while dividend >= (divisor << bit_num):
            bit_num += 1
        quotient = 0
        for i in range(bit_num-1, -1, -1):
            if dividend >= (divisor << i):
                quotient += 1 << i
                dividend -= divisor << i    
        if negative:
            quotient = -quotient
        return min(max(-2147483648, quotient), 2147483647)
    
instance = Solution()
print (instance.divide(dividend , divisor))    