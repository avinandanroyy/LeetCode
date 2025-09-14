class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))

sol = Solution()

print(sol.multiply("2","3"))
#Expected Output : "6"

print(sol.multiply("123","456"))
#Expected Output : "56088"