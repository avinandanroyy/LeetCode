from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        for i in range(size):
            set_col = set()
            for j in range(size):
                if(board[i][j]=="."):
                    continue
                if(board[i][j] in set_col):
                    return False
                set_col.add(board[i][j])

        for i in range(size):
            set_row = set()
            for j in range(size):
                if(board[j][i]=="."):
                    continue
                if(board[j][i] in set_row):
                    return False
                set_row.add(board[j][i])

        for i in range(0, size, 3):
            for j in range(0, size, 3):
                grid_set = set()
                for k in range(3):
                    for l in range(3):
                        if(board[i+k][j+l]=="."):
                            continue
                        if(board[i+k][j+l] in grid_set):
                            return False      
                        grid_set.add(board[i+k][j+l])
        return True

sol = Solution()

print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
#Expected Output : True

print(sol.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

#Expected Output : False

