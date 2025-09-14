from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []

        if not 4 <= n <= 12:
            return []

        def backtrack(start_index: int, parts: List[str]):
            if len(parts) == 4:
                if start_index == n:
                    result.append(".".join(parts))
                return

            for length in range(1, 4):
                if start_index + length > n:
                    break
                
                part_str = s[start_index : start_index + length]
                if s[start_index] == '0' and length > 1:
                    break
                    
                if int(part_str) > 255:
                    break

                parts.append(part_str)
                backtrack(start_index + length, parts)
                parts.pop()

        backtrack(0, [])
        return result


sol = Solution()

print(sol.restoreIpAddresses("25525511135"))
print(sol.restoreIpAddresses("0000"))
print(sol.restoreIpAddresses("101023"))