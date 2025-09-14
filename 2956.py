from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total = n * n
        s = total * (total + 1) // 2
        s2 = total * (total + 1) * (2 * total + 1) // 6

        sn = 0
        s2n = 0

        for row in grid:
            for num in row:
                sn += num
                s2n += num * num

        val1 = s - sn
        val2 = (s2 - s2n) // val1
        x = (val1 + val2) // 2
        y = x - val1

        return [y, x]
    
sol = Solution()
grid = [[1,3],[2,2]]
grid1 = [[9,1,7],[8,9,2],[3,4,6]]
print(sol.findMissingAndRepeatedValues(grid))
# Output: [3, 2] 
print(sol.findMissingAndRepeatedValues(grid1))
# Outpur : [9,5]