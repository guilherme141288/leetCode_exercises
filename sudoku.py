board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            row_set = set()
            for value in row:
                if value == ".":
                    continue
                if value in row_set:
                    return False
                row_set.add(value)

        # Check columns
        for col in range(9):
            col_set = set()
            for row in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                if value in col_set:
                    return False
                col_set.add(value)

        # Check sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()
                for row in range(box_row, box_row+3):
                    for col in range(box_col, box_col+3):
                        value = board[row][col]
                        if value == ".":
                            continue
                        if value in box_set:
                            return False
                        box_set.add(value)

        # All cells are valid
        return True

    

instance = Solution()  
print (instance.isValidSudoku(board))    