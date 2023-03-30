

ransomNote = "a"
magazine = "b"


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = [0] * 26  # array to count the frequency of each character
        for ch in magazine:
            char_count[ord(ch) - ord('a')] += 1  # increment the count of the character

        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            if char_count[idx] <= 0:
                return False  # the character is not present in the magazine string
            char_count[idx] -= 1  # decrement the count of the character

        return True
    

instance = Solution()
print (instance.canConstruct(ransomNote , magazine))    