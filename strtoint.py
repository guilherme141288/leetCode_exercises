s = "42"

class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading and trailing whitespaces
        s = s.strip()
        
        # Check for empty string or only sign character
        if not s or (len(s) == 1 and (s[0] == '+' or s[0] == '-')):
            return 0
        
        # Check if first character is a sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # Convert the remaining string to integer
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                break
        
        # Apply sign and check for integer overflow
        num *= sign
        if num < -2**31:
            return -2**31
        elif num > 2**31 - 1:
            return 2**31 - 1
        else:
            return num


instance = Solution()
print (instance.myAtoi(s))
