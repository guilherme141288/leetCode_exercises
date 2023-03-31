from typing import List

nums = [2,3,1,1,4]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxIndex = 0
        for i in range(n):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex, i + nums[i])
            if maxIndex >= n - 1:
                return True
        return False
    
