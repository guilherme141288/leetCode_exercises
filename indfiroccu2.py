haystack = "sadbutsad"
needle = "sad"

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Build prefix table
        prefix = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[j] != needle[i]:
                j = prefix[j-1]
            if needle[j] == needle[i]:
                j += 1
            prefix[i] = j

        # Match needle in haystack using prefix table
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = prefix[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1

        return -1
    

instance = Solution()
print (instance.strStr(haystack , needle))     