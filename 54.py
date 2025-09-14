from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        
        rowBegin, rowEnd = 0, len(matrix) - 1
        colBegin, colEnd = 0, len(matrix[0]) - 1
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # Traverse Right
            for j in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][j])
            rowBegin += 1
            
            # Traverse Down
            for i in range(rowBegin, rowEnd + 1):
                res.append(matrix[i][colEnd])
            colEnd -= 1
            
            # Traverse Left
            if rowBegin <= rowEnd:
                for j in range(colEnd, colBegin - 1, -1):
                    res.append(matrix[rowEnd][j])
                rowEnd -= 1
            
            # Traverse Up
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[i][colBegin])
                colBegin += 1
        
        return res

if __name__ == "__main__":
    sol = Solution()

    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    print(sol.spiralOrder(matrix1))
    print(sol.spiralOrder(matrix2))