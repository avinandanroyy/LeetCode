from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> List[List[int]]:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i // 3) * 3 + (j // 3)].add(board[i][j])
                else:
                    empties.append((i, j))

        def backtrack(idx=0):
            if idx == len(empties):
                return True
            i, j = empties[idx]
            box_idx = (i // 3) * 3 + (j // 3)
            for ch in map(str, range(1, 10)):
                if ch not in rows[i] and ch not in cols[j] and ch not in boxes[box_idx]:
                    board[i][j] = ch
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[box_idx].add(ch)
                    if backtrack(idx + 1):
                        return True
                    board[i][j] = '.'
                    rows[i].remove(ch)
                    cols[j].remove(ch)
                    boxes[box_idx].remove(ch)
            return False

        backtrack()
        return board

sol  = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(sol.solveSudoku(board))