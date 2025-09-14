from math import ceil

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def pow(x, n):
            result = 1
            while n > 0:
                if n % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                n //= 2
            return result

        even = ceil(n / 2)
        odd = n // 2

        return (pow(5, even) * pow(4, odd)) % MOD
    
sol = Solution()

n1 = 1
print(sol.countGoodNumbers(n1)) #Expected Oupput : 5. Right Answer IS COMING

n2 = 4
print(sol.countGoodNumbers(n2)) #Expected Oupput : 400. Right Answer IS COMING

n3 = 50
print(sol.countGoodNumbers(n3)) #Expected Output :  564908303. Right Answer IS COMING

