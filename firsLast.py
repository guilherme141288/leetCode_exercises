from typing import List

nums = [5,7,7,8,8,10]
target = 8

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
    # Binary search to find the first occurrence of target
        left, right = 0, len(nums)-1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            if nums[mid] == target:
                first = mid
    
    # If target was not found, return [-1, -1]
        if first == -1:
            return [-1, -1]
    
    # Binary search to find the last occurrence of target
        left, right = first, len(nums)-1
        last = first
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] == target:
                last = mid
    
        return [first, last]
    
instance = Solution()  
print (instance.searchRange(nums , target))    
