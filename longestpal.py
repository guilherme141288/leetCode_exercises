s = "babad"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        dp = [[False] * n for _ in range(n)]
        start, end = 0, 0
        
        for i in range(n):
            dp[i][i] = True
            
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) and (i-j <= 2 or dp[j+1][i-1])
                
                if dp[j][i] and i-j > end-start:
                    start, end = j, i
                    
        return s[start:end+1]
    
instance = Solution()
print (instance.longestPalindrome(s))       