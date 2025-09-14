from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        size = 1 << n
        for i in range(size):
            result.append(i ^ (i >> 1))
        return result
    
sol = Solution()

print(sol.grayCode(2))
print(sol.grayCode(1))