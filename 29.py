class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        negative = (dividend < 0) != (divisor < 0)
        
        dividendLong = abs(dividend)
        divisorLong = abs(divisor)
        
        quotient = 0
        
        while dividendLong >= divisorLong:
            shift = 0
            while dividendLong >= (divisorLong << shift):
                shift += 1
            shift -= 1
            quotient += (1 << shift)
            dividendLong -= (divisorLong << shift)
        
        return -quotient if negative else quotient

if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(10, 3))      # Output: 3
    print(sol.divide(7, -3))      # Output: -2
    print(sol.divide(-2147483648, -1))  # Output: 2147483647 (capped)

