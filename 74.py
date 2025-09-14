from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowIdx = self.searchPotentialRow(matrix, target)
        if rowIdx != -1:
            return self.binarySearchOverRow(rowIdx, matrix, target)
        return False

    def searchPotentialRow(self, matrix: list[list[int]], target: int) -> int:
        low = 0
        high = len(matrix) - 1
        idx = len(matrix[0]) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[mid][0] <= target <= matrix[mid][idx]:
                return mid
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def binarySearchOverRow(self, rowIdx: int, matrix: list[list[int]], target: int) -> bool:
        low = 0
        high = len(matrix[rowIdx]) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[rowIdx][mid] == target:
                return True
            elif matrix[rowIdx][mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False

sol = Solution()

print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]]),13) #Output Not Coming
