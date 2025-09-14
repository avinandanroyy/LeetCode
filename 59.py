from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        num = 1
        left, right, top, bottom = 0, n-1, 0, n-1

        while left <= right and top <= bottom:
            # Fill top row
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            top += 1

            # Fill right column
            for i in range(top, bottom+1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # Fill bottom row
            if top <= bottom:
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1

            # Fill left column
            if left <= right:
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix

solution = Solution()
print(solution.generateMatrix(3)) #Expected Output: [[1,2,3],[8,9,4],[7,6,5]]
print(solution.generateMatrix(1)) #Expected Output: [[1]]