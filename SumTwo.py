


from typing import List

numbers = [2, 7, 11, 15]
target_value = 9
complement_indices = {}

class Solution:
    def findIndicesForTwoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in complement_indices:
                # If it is, return the indices of the two numbers
                return [complement_indices[complement], i]
            
            # If the complement is not in the dictionary, add the current number and its index to the dictionary
            complement_indices[num] = i
        
        # If no two numbers add up to the target, return an empty list
        return []

solver = Solution()
print(solver.findIndicesForTwoSum(numbers, target_value))

