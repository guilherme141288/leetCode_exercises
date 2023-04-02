
from typing import List

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        def backtrack(i, j, index):
            if index == len(word): # if all characters have been matched, return True
                return True

            if i < 0 or i >= m or j < 0 or j >= n: # if the cell is outside the board, return False
                return False

            if visited[i][j] or board[i][j] != word[index]: # if the cell has already been visited or the character does not match, return False
                return False

            visited[i][j] = True # mark the current cell as visited
            found = backtrack(i+1, j, index+1) or backtrack(i-1, j, index+1) or backtrack(i, j+1, index+1) or backtrack(i, j-1, index+1) # recursively check adjacent cells
            visited[i][j] = False # mark the current cell as unvisited

            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0): # start backtracking from each cell that matches the first character of the word
                    return True

        return False
    
instance = Solution()
print (instance.exist(board , word))    
 