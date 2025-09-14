from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        if numRows == 0:
            return result

        firstRow = [1]
        result.append(firstRow)

        if numRows == 1:
            return result

        for i in range(1, numRows):
            prevRow = result[i - 1]

            row = [1]
            for j in range(i - 1):
                row.append(prevRow[j] + prevRow[j + 1])
            row.append(1)

            result.append(row)

        return result

sol = Solution()
print(sol.generate(5))