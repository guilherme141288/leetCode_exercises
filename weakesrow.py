mat = [[1,1,0,0,0],
       [1,1,1,1,0],
       [1,0,0,0,0],
       [1,1,0,0,0],
       [1,1,1,1,1]]

k = 3       

from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for i in range(len(mat)):
            rows.append((i, sum(mat[i])))
    
        rows.sort(key=lambda x: (x[1], x[0]))
    
        result = []
        for i in range(k):
            result.append(rows[i][0])
    
        return result
    
instance = Solution()
print(instance.kWeakestRows(mat , k))    