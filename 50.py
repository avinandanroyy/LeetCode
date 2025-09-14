class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        
        result = 1.0
        while n != 0:
            if n % 2 != 0:
                result *= x
            x *= x
            n //= 2
        return result


sol = Solution()

print(sol.myPow(2.00000,10))
print(sol.myPow(2.10000,3))
print(sol.myPow(2.00000,-2))