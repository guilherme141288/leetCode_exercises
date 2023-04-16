n = 1

class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Recursive case
        prev_str = self.countAndSay(n - 1)
        curr_str = ""
        count = 1
        for i in range(1, len(prev_str)):
            if prev_str[i] == prev_str[i-1]:
                count += 1
            else:
                curr_str += str(count) + prev_str[i-1]
                count = 1
        curr_str += str(count) + prev_str[-1]
        return curr_str
    
instance = Solution()
print (instance.countAndSay(n))    