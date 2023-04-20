from typing import List

nums = [1,2,3]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       
        def backtrack(first):
            if first == n:
            # add the current permutation to the result
                result.append(nums[:])
            for i in range(first, n):
            # swap the first element with each element starting from first
                nums[first], nums[i] = nums[i], nums[first]
            # recurse on the remaining elements
                backtrack(first + 1)
            # backtrack by swapping back the elements
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        result = []
        backtrack(0)
        return result
    
instance = Solution()
print (instance.permute(nums))    
