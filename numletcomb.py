
digits = "23"

from typing import List

class Solution:
    def letterCombinations(self , digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }

        def backtrack(index, combination):
            if index == len(digits):
                output.append(combination)
            else:
                for letter in mapping[digits[index]]:
                    backtrack(index + 1, combination + letter)

        output = []
        backtrack(0, "")
        return output


instance = Solution()
print (instance.letterCombinations(digits))
