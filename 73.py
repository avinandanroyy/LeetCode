from typing import List

class Solution:
    def setZeros(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        rowZero = False
        colZero = False

        # Check if first column needs to be zero
        for r in range(rows):
            if matrix[r][0] == 0:
                colZero = True
                break

        # Check if first row needs to be zero
        for c in range(cols):
            if matrix[0][c] == 0:
                rowZero = True
                break

        # Use first row and column as markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero out cells based on markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Zero out first column if needed
        if colZero:
            for r in range(rows):
                matrix[r][0] = 0

        # Zero out first row if needed
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0

        return matrix

if __name__ == "__main__":
    sol = Solution()

    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    print(sol.setZeros(matrix1))

    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(sol.setZeros(matrix2))
