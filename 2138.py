from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        groups = (n + k - 1) // k
        result = []

        for i in range(groups):
            start = i * k
            chunk = ""

            for j in range(k):
                index = start + j
                if index < n:
                    chunk += s[index]
                else:
                    chunk += fill

            result.append(chunk)

        return result

sol = Solution()
print(sol.divideString("abcdefghi", 3, 'x'))  
# Output: ['abc', 'def', 'ghi']

print(sol.divideString("abcdefghij", 3, 'x'))  
# Output: ['abc', 'def', 'ghi', 'jxx']
