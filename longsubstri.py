s = "abcabcbb"


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_len = 0
        chars = set()

    # iterate through the string
        while end < len(s):
            # check if current character is already in the set
            if s[end] not in chars:
            # if not, add it to the set and expand the window
                chars.add(s[end])
                end += 1
                max_len = max(max_len, end - start)
            else:
            # if yes, remove the first character from the set and shrink the window
                chars.remove(s[start])
                start += 1

        return max_len
    
instance = Solution()
print (instance.lengthOfLongestSubstring(s))    