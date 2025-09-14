from typing import List

class Solution:
    def rotateImage(self, matrix: List[List[int]]) -> List[List[int]]:
        left = 0
        right = len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                topleft = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i ][right]
                matrix[top + i][right] = topleft

            right -= 1
            left += 1

        return matrix
    
if __name__ == "__main__":
    sol = Solution()

    matrix1 = [[1,2,3],[4,5,6],[7,8,9]] 
    print(sol.rotateImage(matrix1))

    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] 
    print(sol.rotateImage(matrix2))