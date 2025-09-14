from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        value = 1
        
        row.append(1)
        
        for i in range(1, rowIndex + 1):
            value = value * (rowIndex - i + 1) // i
            row.append(value)
            
        return row
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.getRow(3))
    print(sol.getRow(0))
    print(sol.getRow(1))