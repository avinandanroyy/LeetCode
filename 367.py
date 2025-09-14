class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

sol = Solution()
print(sol.isPerfectSquare(16))  # True
print(sol.isPerfectSquare(14))  # False
