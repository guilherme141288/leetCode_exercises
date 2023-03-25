x = 123


class Solution:
    def reverse(self, x: int) -> int:
    # handle negative numbers by flipping the sign and processing as positive
        sign = -1 if x < 0 else 1
        x *= sign

    # reverse the digits of x
        rev = 0
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
            if rev > 2**31 - 1 or rev < -2**31:
                return 0
            

        return sign * rev
    
instance = Solution()
print (instance.reverse(x))    