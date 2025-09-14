class Solution:

    def reverse(self, x: int) -> int:
        res = 0
        is_negative = x  < 0
        x = abs(x)

        while x:
            digit = x % 10
            x //= 10

            if res > 214748364 or (res == 214748364 and digit > 7 ):
                return 0
            
            res = res * 10 + digit
        
        return -res if is_negative else res
    
if __name__ == "__main__":
    sol = Solution()

    #Example 1
    x = 123
    print(sol.reverse(x))

    #Example 2 
    num = -12312
    print(sol.reverse(num))