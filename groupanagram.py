from typing import List

strs = ["eat","tea","tan","ate","nat","bat"]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

    # Loop through each string in the array
        for s in strs:
        # Sort the string and use it as a key in the hash table
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagrams:
            # If the key already exists, append the current string to the value
                anagrams[sorted_s].append(s)
            else:
            # If the key doesn't exist, create a new key-value pair
                anagrams[sorted_s] = [s]

        # Return the list of anagram groups
        return list(anagrams.values())
    

instance = Solution()
print (instance.groupAnagrams(strs))    