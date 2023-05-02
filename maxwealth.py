accounts = [[1,2,3],[3,2,1]]
from typing import List
class Solution:
    
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth
    
instance = Solution()
print (instance.maximumWealth(accounts))    