candidates = [2,3,6,7]
target = 7

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], result)
        return result
    
    def backtrack(self, candidates, target, start, combination, result):
        if target < 0:
            return
        elif target == 0:
            result.append(combination)
            return
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                self.backtrack(candidates, target - candidates[i], i, combination + [candidates[i]], result)

instance = Solution()
print (instance.combinationSum(candidates , target))                